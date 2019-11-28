# Description

PDF Reader is a plugin for extracting text from a PDF file.

This plugin utilizes a python package called [PyPDF2](https://pypi.org/project/PyPDF2/).

# Key Features

* Extract text from a PDF document

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Extract Text

This action is used to extract text from a PDF file.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|contents|bytes|None|True|PDF file to extract text from|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|string|False|Text extracted from PDF file|

Example output:

```

{
"output": "Functional Resume Sample  John W. Smith  2002 Front Range Way Fort Collins, CO 80525  jwsmith@colostate.edu  Career Summary  Four years experience in early childhood development with a diverse background in the care of special needs children and adults.    Adult Care Experience   Determined work placement for 150 special needs adult clients.   Maintained client databases and records.   Coordinated client contact with local health care professionals on a monthly basis.      Managed 25 volunteer workers.      Childcare Experience   Coordinated service assignments for 20 part-time counselors and 100 client families.  Oversaw daily activity and outing planning for 100 clients.   Assisted families of special needs clients with researching financial assistance and healthcare.  Assisted teachers with managing daily classroom activities.     Oversaw daily and special student activities.      Employment History   1999-2002 Counseling Supervisor, The Wesley Center, Little Rock, Arkansas.    1997-1999 Client Specialist, Rainbow Special Care Center, Little Rock, Arkansas  1996-1997 Teacher's Assistant, Cowell Elementary, Conway, Arkansas      Education  University of Arkansas at Little Rock, Little Rock, AR    BS in Early Childhood Development (1999)  BA in Elementary Education (1998)  GPA (4.0 Scale):  Early Childhood Development 3.8, Elementary Education 3.5, Overall 3.4.   Dean's List, Chancellor's List"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Support web server mode
* 0.1.0 - Initial plugin

# Links

## References

* [PyPDF2](https://pypi.org/project/PyPDF2/)

