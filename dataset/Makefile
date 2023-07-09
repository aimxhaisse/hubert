SOURCES_DIR := sources/
REPOS := k8s golang geth

# Basic rules.

all: sync filter

sync: $(REPOS)

stats:
	@echo "Number of Golang files"
	@find $(SOURCES_DIR) -name '*.go' | wc -l
	@echo "Number of Golang lines"
	@find $(SOURCES_DIR) -name '*.go' -type f -exec cat {} \; | wc -l

filter:
	find $(SOURCES_DIR) -type f ! -name '*.go' -delete

# Training codebases we learn upon.

k8s: sources/k8s
sources/k8s:
	git clone https://github.com/kubernetes/kubernetes.git $@

golang: sources/golang
sources/golang:
	git clone https://github.com/golang/go $@

geth: sources/geth
sources/geth:
	git clone https://github.com/ethereum/go-ethereum.git $@

# Misc.

.PHONY: sync filter $(REPOS)
