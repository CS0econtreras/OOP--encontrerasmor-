PLANTUML = java -jar ~/plantuml.jar
DOCS = docs

all: create_docs create_uml check_types localtest

check_types:
ifeq ($(shell which mypy), )
	@echo "mypy not found. Installing mypy..."
	pip install mypy
endif
	mypy --disallow-untyped-defs --strict main.py 
	mypy --disallow-untyped-defs --strict cups.py
	mypy --disallow-untyped-defs --strict kattis.py 
	@echo "Type checking done."

create_doc_folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

create_docs: create_doc_folder
	pdoc --force -o docs main.py cups.py kattis.py # creates .md docs inside docs
	pdoc --force --html -o docs main.py cups.py kattis.py # creates html docs inside docs
	@echo "html docs created and saved in $(DOCS)"

localtest:
	cat data/data.in | python main.py | diff - data/data.ans
	
	@echo "Program worked on file"

create_uml: create_doc_folder
	$(PLANTUML) uml/kattis.plantuml
	$(PLANTUML) uml/cups.plantuml
	$(PLANTUML) uml/Main.plantuml
	@echo "UML diagrams created and saved in uml folder"
