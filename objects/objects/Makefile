PLANTUML = java -jar ~/plantuml.jar
DOCS = docs

all: check_types create_docs localtest create_uml
	@echo "All done!"
	
localtest:
	cat data/data.in | python main.py | diff - data/data.ans
	
	@echo "Program worked on file"

create_doc_folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

create_docs: create_doc_folder
	pdoc --force -o docs main.py polygonClass.py # creates .md docs inside docs
	pdoc --force --html -o docs main.py polygonClass.py # creates html docs inside docs
	@echo "html docs created and saved in $(DOCS)"

check_types:
# use shell command which to check if mypy is installed and is in $PATH
ifeq ($(shell which mypy), )
	@echo "mypy not found. Installing mypy..."
	pip install mypy
endif
	mypy --disallow-untyped-defs --strict main.py 
	mypy --disallow-untyped-defs --strict polygonClass.py 
	@echo "Type checking done."

create_uml: create_doc_folder
	$(PLANTUML) uml/polygonClass.plantuml
	$(PLANTUML) uml/Main.plantuml
	$(PLANTUML) uml/solution.plantuml
	@echo "UML diagrams created and saved in uml folder"


