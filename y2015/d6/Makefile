# Makefile

RUSTC  ?= rustc
SRC     = main.rs
OUTDIR  = out
BIN     = $(OUTDIR)/main

.PHONY: all build run clean

all: build

$(OUTDIR):
	@mkdir -p $(OUTDIR)

$(BIN): $(SRC) | $(OUTDIR)
	$(RUSTC) $(SRC) -o $(BIN)

build: $(BIN)
	@echo "Built $(BIN)"

run: build
	@$(BIN) $(ARGS)

clean:
	@rm -rf $(OUTDIR)