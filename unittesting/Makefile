PLANTUML = java -jar ~/plantuml.jar
DOCS = docs

all: create_docs create_uml check_types localtest unittest
	@echo "All done!"

create_doc_folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

create_docs: create_doc_folder
	pdoc --force -o docs main.py palindrom.py # creates .md docs inside docs
	pdoc --force --html -o docs main.py palindrom.py # creates html docs inside docs
	@echo "html docs created and saved in $(DOCS)"

create_uml: create_doc_folder
	$(PLANTUML) uml/solution.plantuml
	$(PLANTUML) uml/palindrom.plantuml
	$(PLANTUML) uml/Main.plantuml
	@echo "UML diagrams created and saved in uml folder"

check_types:
	mypy --disallow-untyped-defs --strict main.py 
	mypy --disallow-untyped-defs --strict palindrom.py 
	@echo "Type checking done."

localtest:
	cat data/m0000.in | python main.py | diff - data/m0000.ans
	cat data/m0001.in | python main.py | diff - data/m0001.ans
	cat data/m0002.in | python main.py | diff - data/m0002.ans
	cat data/m0003.in | python main.py | diff - data/m0003.ans
	cat data/m0004.in | python main.py | diff - data/m0004.ans
	cat data/m0005.in | python main.py | diff - data/m0005.ans
	@echo "Program worked on file"

unittest:
	python main_unittest.py
	python palindrom_unittest.py
	@echo "Unittest done."