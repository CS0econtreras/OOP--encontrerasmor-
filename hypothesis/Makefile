PLANTUML = java -jar ~/plantuml.jar
DOCS = docs

all: create_docs create_uml check_types localtest unittest
	@echo "All done!"
	
create_doc_folder:
	@mkdir -p $(DOCS) # creates all folder(s) if not exists

create_docs: create_doc_folder
	pdoc --force -o docs main.py movies.py # creates .md docs inside docs
	pdoc --force --html -o docs main.py movies.py # creates html docs inside docs
	@echo "html docs created and saved in $(DOCS)"

check_types:
	mypy --disallow-untyped-defs --strict main.py 
	mypy --disallow-untyped-defs --strict movies.py 
	@echo "Type checking done."

create_uml: create_doc_folder
	$(PLANTUML) uml/solution.plantuml
	$(PLANTUML) uml/movies.plantuml
	$(PLANTUML) uml/main.plantuml
	@echo "UML diagrams created and saved in uml folder"

localtest:
	cat data/1.in | python main.py | diff - data/1.ans
	cat data/1.in | python main.py | diff - data/1.ans
	cat data/1.in | python main.py | diff - data/1.ans
	@echo "Program worked on file"

unittest:
	python test_main.py
	python test_movie.py
	@echo "Unittest done."

