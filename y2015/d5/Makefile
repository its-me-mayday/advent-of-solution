.PHONY: build run clean

OUT := out
SRC := .
MAIN := d5.Main

build:
	mkdir -p $(OUT)
	javac -d $(OUT) $(shell find $(SRC) -name '*.java')

run: build
	java -cp $(OUT) $(MAIN)

clean:
	rm -rf $(OUT)