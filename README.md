# HospitalGeneratorRDF

aaa

## 1. Data Structure

aaa


## 2.Installation
The source code is currently hosted on [github.com/LorenaPujante/HospitalGeneratorRDF](https://github.com/LorenaPujante/HospitalGeneratorRDF).

The program is in Python 3.10, and no external packages are needed.


## 3. Execution and Configuration Params
To run the program, in the terminal, go to the folder containing the program and run: `python main.py`

The main function receives as parameters for configuring the result the following:
- _X_: aaa.
- _Y_: aaa.

For example, if we execute: `main(1,2)`, the program will ...

In the file _main.py_, the function `main()` has a set of tests for executing the program with different configuration parameters. These parameters can be changed in this function.
aaa


## 4. Outcomes
After running the program, the following folders are created:
- _OutputCSV_: Folder with the nodes and edges of the graph in the form of CSV files.
	- Nodes and edges are in different folders: `OutputCSV/Classes` (nodes) and `OutputCSV/CSV` (edges). Each class of nodes and edges is in a separate file.
- _OutputRDF_: Folder with the nodes and edges of the RDF knowledge graph in the form of N-Triples files.
	- Nodes and edges are in different folders: `OutputRDF/Classes` (nodes) and `OutputRDF/CSV` (edges). Each class of nodes and edges is in a separate file. Inside each folder, there also is a file with the union of all the nodes (`OutputRDF/Classes/Classes_complete.nt`) and the union of all the edges (`OutputRDF/Relations/Relations_complete.nt`), respectively. Finally, the file `OutputRDF/data_complete.*.nt` contains the nodes and edges' union.
- _OutputRDF_star_: Folder with the nodes and edges of the RDF* knowledge graph in the form of N-Triples files (nodes) and Turtle files (edges).
	- Nodes and edges are in different folders: `OutputRDF_star/Classes` (nodes) and `OutputRDF_star/CSV` (edges). Each class of nodes and edges is in a separate file. Inside each folder, there also is a file with the union of all the nodes (`/Classes.*/Classes_complete.nt`) and the union of all the edges (`OutputRDF_star/Relations.*/Relations_complete.ttl`), respectively. Finally, the file `OutputRDF_star/data_complete.ttl` contains the nodes and edges' union.
- _OutputSummary_: Folder with two summary files:
  - _EpisodeSummary.txt_: This file shows for each patients how many Episodes and Events with their _description_, _id_ and _start_ and _end dates_. For Events, it also shows their subclass and to which Bed they are connected.
  - _HospitalSummary.txt_: This file shows a list with all the Services, HopitalizationUnits and Locations of the hospital. For each element, it presents its id, description and several lists with all the other elements of the spatial dimmension to which it is connected.     

Repeated runs will replace existing files.
