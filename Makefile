CODEGEN_OPTIONS = --input-file-type auto --snake-case-field --target-python-version 3.9 --allow-population-by-field-name
K8S_OPENAPI_URL = https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json
TKN_OPENAPI_URL = https://raw.githubusercontent.com/tektoncd/pipeline/main/pkg/apis/pipeline/v1beta1/swagger.json

ASSETS_DIR=$(shell pwd)/tmp

.PHONY: k8s-manifests tkn-manifests bases-codegen clean


all: k8s-manifests k8s-codegen


k8s-manifests:
	mkdir -p ${ASSETS_DIR}
	test -f ${ASSETS_DIR}/swagger.json || curl -sSLo ${ASSETS_DIR}/swagger.json ${K8S_OPENAPI_URL}

k8s-codegen:
	datamodel-codegen --output src/generated ${CODEGEN_OPTIONS} --input ${ASSETS_DIR}/swagger.json

# NOTE Tekton CRD needs additional adjustment for normalization.
tkn-manifests:
	mkdir -p ${ASSETS_DIR}
	test -f ${ASSETS_DIR}/tekton.swagger.json || curl -sSLo ${ASSETS_DIR}/tekton.swagger.json ${TKN_OPENAPI_URL}

tkn-codegen:
	datamodel-codegen --output src/generated ${CODEGEN_OPTIONS} --input ${ASSETS_DIR}/tekton.swagger.json

clean:
	rm -f ${ASSETS_DIR}/swagger.json ${ASSETS_DIR}/tekton.swagger.json
