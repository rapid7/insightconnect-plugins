
# Pastebin

## About

[Pastebin](http://pastebin.com/) is a website where you can store any text online
for easy sharing. The website is mainly used by programmers to store pieces of
sources code or configuration information, but anyone is more than welcome to
paste any type of text. The idea behind the site is to make it more convenient
for people to share large amounts of text online.

## Actions

### Paste

This action is used to post to Pastebin.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|paste_private|string|None|False|Privacy setting of paste|['private', 'unlisted', 'public']|
|paste_format|string|text|False|Which language format is the paste in|['4CS', '6502 ACME Cross Assembler', '6502 Kick Assembler', '6502 TASM/64TASS', 'ABAP', 'ActionScript', 'ActionScript 3', 'Ada', 'AIMMS', 'ALGOL 68', 'Apache Log', 'AppleScript', 'APT Sources', 'ARM', 'ASM (NASM)', 'ASP', 'Asymptote', 'autoconf', 'Autohotkey', 'Autolt', 'Avisynth', 'Awk', 'BASCOM AVR', 'Bash', 'Basic4GL', 'Batch', 'BibTeX', 'Blitz Basic', 'Blitz3D', 'BLitzMax', 'BNF', 'BOO', 'Brainfuck', 'C', 'C (WinAPI)', 'C for Macs', 'C Intermediate Language', 'C#', 'C++', 'C++ (WinAPI)', 'C++ (with Qt extensions)', 'C: Loadrunner', 'CAD DCL', 'CAD Lisp', 'CFDG', 'ChaiScript', 'Chapel', 'Clojre', 'Clone C', 'Clone C++', 'CMake', 'COBOL', 'CoffeeScript', 'ColdFusion', 'CSS', 'Cuesheet', 'D', 'Dart', 'DCL', 'DCPU-16', 'DCS', 'Delphi', 'Delphi Prism (Oxygene)', 'Diff', 'DIV', 'DOT', 'E', 'Easytrieve', 'ECMAScript', 'Eiffel', 'Email', 'EPC', 'Erlang', 'Euphoria', 'F#', 'Falcon', 'Filemaker', 'FO Language', 'Formula One', 'Fortran', 'FreeBasic', 'FreeSWITCH', 'GAMBAS', 'Game Maker', 'GDB', 'Genero', 'Genie', 'GetText', 'Go', 'Groovy', 'GwBasic', 'Haskell', 'Haxe', 'HicEst', 'HQ9 Plus', 'HTML', 'HTML 5', 'Icon', 'IDL', 'INI file', 'Inno Script', 'INTERCAL', 'IO', 'ISPF Panel Definition', 'J', 'Java', 'Java 5', 'JavaScript', 'JCL', 'jQuery', 'JSON', 'Julia', 'KiXtart', 'Latex', 'LDIF', 'Liberty BASIC', 'Linden Scripting', 'Lisp', 'LLVM', 'Loco Basic', 'Logtalk', 'LOL Code', 'Lotus Formulas', 'Lotus Script', 'LScrpt', 'Lua', 'M68000 Assembler', 'MagikSF', 'Make', 'MapBasic', 'Markdown', 'MatLab', 'mIRC', 'MIX Assembler', 'Modula 2', 'Modula 3', 'Motorola 68000 HiSoft Dev', 'MPASM', 'MXML', 'MySQL', 'Nagios', 'NetRexx', 'newLISP', 'Nginx', 'Nimrod', 'None', 'NullSoft Installer', 'Oberon 2', 'Objeck Programming Language', 'Objective C', 'OCalm Brief', 'OCaml', 'Octave', 'Open Object Rexx', 'OpenBSF PACKET FILTER', 'OpenGL Shading', 'Openoffice BASIC', 'Oracle 11', 'Oracle 8', 'Oz', 'ParaSail', 'PARI/GP', 'Pascal', 'Pawn', 'PCRE', 'Per', 'Perl', 'Perl 6', 'PHP', 'PHP Brief', 'Pic 16', 'Pike', 'Pixel Bender', 'PL/I', 'PL/SQL', 'PostgreSQL', 'PostScript', 'POV-Ray', 'Power Shell', 'PowerBuilder', 'ProFTPd', 'Progress', 'Prolog', 'Properties', 'ProvideX', 'Puppet', 'PureBasic', 'PyCon', 'Python', 'Python for S60', 'q/kdb+', 'QBasic', 'QML', 'R', 'Racket', 'Rails', 'RBScript', 'REBOL', 'REG', 'Rexx', 'Robots', 'RPM Spec', 'Ruby', 'Ruby Gnuplot', 'Rust', 'SAS', 'Scala', 'Scheme', 'Scilab', 'SCL', 'SdlBasic', 'Smalltalk', 'Smarty', 'SPARK', 'SPARQL', 'SQF', 'SQL', 'StandardML', 'StoneScript', 'SuperCollider', 'Swift', 'SystemVerilog', 'T-SQL', 'TCL', 'Tera Term', 'text', 'thinBasic', 'TypoScript', 'Unicon', 'UnrealScript', 'UPC', 'Urbi', 'Vala', 'VB.NET', 'VBScript', 'Vedit', 'VeriLog', 'VHDL', 'VIM', 'Visual Pro Log', 'VisualBasic', 'VisualFoxPro', 'WhiteSpace', 'WHOIS', 'Winbatch', 'XBasic', 'XML', 'Xorg Config', 'XPP', 'YAML', 'Z80 Assembler', 'ZXBasic']|
|paste_name|string|None|False|Title of paste|None|
|paste_expire_date|string|None|False|When should the paste expire|['Never', '10 Minutes', '1 Hour', '1 Day', '1 Week', '2 Weeks', '1 Month']|
|text|string|None|True|Body of the paste|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|None|
|timestamp|date|False|None|

### Scrape

This action is used to scrape for most recent posts on Pastebin with a user provided search query.
Scraping require a Pastebin Pro account.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pattern|string|None|True|Plain text or regex to be used to find matches|None|
|limit|integer|100|True|Number of pastes pulled per minute (100 is standard)|None|
|language|string|All|True|Files in which language format should be scraped|['All', '4CS', '6502 ACME Cross Assembler', '6502 Kick Assembler', '6502 TASM/64TASS', 'ABAP', 'ActionScript', 'ActionScript 3', 'Ada', 'AIMMS', 'ALGOL 68', 'Apache Log', 'AppleScript', 'APT Sources', 'ARM', 'ASM (NASM)', 'ASP', 'Asymptote', 'autoconf', 'Autohotkey', 'Autolt', 'Avisynth', 'Awk', 'BASCOM AVR', 'Bash', 'Basic4GL', 'Batch', 'BibTeX', 'Blitz Basic', 'Blitz3D', 'BLitzMax', 'BNF', 'BOO', 'Brainfuck', 'C', 'C (WinAPI)', 'C for Macs', 'C Intermediate Language', 'C#', 'C++', 'C++ (WinAPI)', 'C++ (with Qt extensions)', 'C: Loadrunner', 'CAD DCL', 'CAD Lisp', 'CFDG', 'ChaiScript', 'Chapel', 'Clojre', 'Clone C', 'Clone C++', 'CMake', 'COBOL', 'CoffeeScript', 'ColdFusion', 'CSS', 'Cuesheet', 'D', 'Dart', 'DCL', 'DCPU-16', 'DCS', 'Delphi', 'Delphi Prism (Oxygene)', 'Diff', 'DIV', 'DOT', 'E', 'Easytrieve', 'ECMAScript', 'Eiffel', 'Email', 'EPC', 'Erlang', 'Euphoria', 'F#', 'Falcon', 'Filemaker', 'FO Language', 'Formula One', 'Fortran', 'FreeBasic', 'FreeSWITCH', 'GAMBAS', 'Game Maker', 'GDB', 'Genero', 'Genie', 'GetText', 'Go', 'Groovy', 'GwBasic', 'Haskell', 'Haxe', 'HicEst', 'HQ9 Plus', 'HTML', 'HTML 5', 'Icon', 'IDL', 'INI file', 'Inno Script', 'INTERCAL', 'IO', 'ISPF Panel Definition', 'J', 'Java', 'Java 5', 'JavaScript', 'JCL', 'jQuery', 'JSON', 'Julia', 'KiXtart', 'Latex', 'LDIF', 'Liberty BASIC', 'Linden Scripting', 'Lisp', 'LLVM', 'Loco Basic', 'Logtalk', 'LOL Code', 'Lotus Formulas', 'Lotus Script', 'LScrpt', 'Lua', 'M68000 Assembler', 'MagikSF', 'Make', 'MapBasic', 'Markdown', 'MatLab', 'mIRC', 'MIX Assembler', 'Modula 2', 'Modula 3', 'Motorola 68000 HiSoft Dev', 'MPASM', 'MXML', 'MySQL', 'Nagios', 'NetRexx', 'newLISP', 'Nginx', 'Nimrod', 'None', 'NullSoft Installer', 'Oberon 2', 'Objeck Programming Language', 'Objective C', 'OCalm Brief', 'OCaml', 'Octave', 'Open Object Rexx', 'OpenBSF PACKET FILTER', 'OpenGL Shading', 'Openoffice BASIC', 'Oracle 11', 'Oracle 8', 'Oz', 'ParaSail', 'PARI/GP', 'Pascal', 'Pawn', 'PCRE', 'Per', 'Perl', 'Perl 6', 'PHP', 'PHP Brief', 'Pic 16', 'Pike', 'Pixel Bender', 'PL/I', 'PL/SQL', 'PostgreSQL', 'PostScript', 'POV-Ray', 'Power Shell', 'PowerBuilder', 'ProFTPd', 'Progress', 'Prolog', 'Properties', 'ProvideX', 'Puppet', 'PureBasic', 'PyCon', 'Python', 'Python for S60', 'q/kdb+', 'QBasic', 'QML', 'R', 'Racket', 'Rails', 'RBScript', 'REBOL', 'REG', 'Rexx', 'Robots', 'RPM Spec', 'Ruby', 'Ruby Gnuplot', 'Rust', 'SAS', 'Scala', 'Scheme', 'Scilab', 'SCL', 'SdlBasic', 'Smalltalk', 'Smarty', 'SPARK', 'SPARQL', 'SQF', 'SQL', 'StandardML', 'StoneScript', 'SuperCollider', 'Swift', 'SystemVerilog', 'T-SQL', 'TCL', 'Tera Term', 'text', 'thinBasic', 'TypoScript', 'Unicon', 'UnrealScript', 'UPC', 'Urbi', 'Vala', 'VB.NET', 'VBScript', 'Vedit', 'VeriLog', 'VHDL', 'VIM', 'Visual Pro Log', 'VisualBasic', 'VisualFoxPro', 'WhiteSpace', 'WHOIS', 'Winbatch', 'XBasic', 'XML', 'Xorg Config', 'XPP', 'YAML', 'Z80 Assembler', 'ZXBasic']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|paste_list|[]object|False|None|

## Triggers

### Scraping

This trigger is used to scrape most recent pastes every specified interval for a given pattern.
Scraping require a Pastebin Pro account.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|pattern|string|None|True|Plain text or regex to be used to find matches|None|
|frequency|integer|300|False|Poll frequency in seconds|None|
|limit|integer|100|False|None|None|
|language|string|All|True|Files in which language format should be scraped|['All', '4CS', '6502 ACME Cross Assembler', '6502 Kick Assembler', '6502 TASM/64TASS', 'ABAP', 'ActionScript', 'ActionScript 3', 'Ada', 'AIMMS', 'ALGOL 68', 'Apache Log', 'AppleScript', 'APT Sources', 'ARM', 'ASM (NASM)', 'ASP', 'Asymptote', 'autoconf', 'Autohotkey', 'Autolt', 'Avisynth', 'Awk', 'BASCOM AVR', 'Bash', 'Basic4GL', 'Batch', 'BibTeX', 'Blitz Basic', 'Blitz3D', 'BLitzMax', 'BNF', 'BOO', 'Brainfuck', 'C', 'C (WinAPI)', 'C for Macs', 'C Intermediate Language', 'C#', 'C++', 'C++ (WinAPI)', 'C++ (with Qt extensions)', 'C: Loadrunner', 'CAD DCL', 'CAD Lisp', 'CFDG', 'ChaiScript', 'Chapel', 'Clojre', 'Clone C', 'Clone C++', 'CMake', 'COBOL', 'CoffeeScript', 'ColdFusion', 'CSS', 'Cuesheet', 'D', 'Dart', 'DCL', 'DCPU-16', 'DCS', 'Delphi', 'Delphi Prism (Oxygene)', 'Diff', 'DIV', 'DOT', 'E', 'Easytrieve', 'ECMAScript', 'Eiffel', 'Email', 'EPC', 'Erlang', 'Euphoria', 'F#', 'Falcon', 'Filemaker', 'FO Language', 'Formula One', 'Fortran', 'FreeBasic', 'FreeSWITCH', 'GAMBAS', 'Game Maker', 'GDB', 'Genero', 'Genie', 'GetText', 'Go', 'Groovy', 'GwBasic', 'Haskell', 'Haxe', 'HicEst', 'HQ9 Plus', 'HTML', 'HTML 5', 'Icon', 'IDL', 'INI file', 'Inno Script', 'INTERCAL', 'IO', 'ISPF Panel Definition', 'J', 'Java', 'Java 5', 'JavaScript', 'JCL', 'jQuery', 'JSON', 'Julia', 'KiXtart', 'Latex', 'LDIF', 'Liberty BASIC', 'Linden Scripting', 'Lisp', 'LLVM', 'Loco Basic', 'Logtalk', 'LOL Code', 'Lotus Formulas', 'Lotus Script', 'LScrpt', 'Lua', 'M68000 Assembler', 'MagikSF', 'Make', 'MapBasic', 'Markdown', 'MatLab', 'mIRC', 'MIX Assembler', 'Modula 2', 'Modula 3', 'Motorola 68000 HiSoft Dev', 'MPASM', 'MXML', 'MySQL', 'Nagios', 'NetRexx', 'newLISP', 'Nginx', 'Nimrod', 'None', 'NullSoft Installer', 'Oberon 2', 'Objeck Programming Language', 'Objective C', 'OCalm Brief', 'OCaml', 'Octave', 'Open Object Rexx', 'OpenBSF PACKET FILTER', 'OpenGL Shading', 'Openoffice BASIC', 'Oracle 11', 'Oracle 8', 'Oz', 'ParaSail', 'PARI/GP', 'Pascal', 'Pawn', 'PCRE', 'Per', 'Perl', 'Perl 6', 'PHP', 'PHP Brief', 'Pic 16', 'Pike', 'Pixel Bender', 'PL/I', 'PL/SQL', 'PostgreSQL', 'PostScript', 'POV-Ray', 'Power Shell', 'PowerBuilder', 'ProFTPd', 'Progress', 'Prolog', 'Properties', 'ProvideX', 'Puppet', 'PureBasic', 'PyCon', 'Python', 'Python for S60', 'q/kdb+', 'QBasic', 'QML', 'R', 'Racket', 'Rails', 'RBScript', 'REBOL', 'REG', 'Rexx', 'Robots', 'RPM Spec', 'Ruby', 'Ruby Gnuplot', 'Rust', 'SAS', 'Scala', 'Scheme', 'Scilab', 'SCL', 'SdlBasic', 'Smalltalk', 'Smarty', 'SPARK', 'SPARQL', 'SQF', 'SQL', 'StandardML', 'StoneScript', 'SuperCollider', 'Swift', 'SystemVerilog', 'T-SQL', 'TCL', 'Tera Term', 'text', 'thinBasic', 'TypoScript', 'Unicon', 'UnrealScript', 'UPC', 'Urbi', 'Vala', 'VB.NET', 'VBScript', 'Vedit', 'VeriLog', 'VHDL', 'VIM', 'Visual Pro Log', 'VisualBasic', 'VisualFoxPro', 'WhiteSpace', 'WHOIS', 'Winbatch', 'XBasic', 'XML', 'Xorg Config', 'XPP', 'YAML', 'Z80 Assembler', 'ZXBasic']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|paste|object|False|None|

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|False|Pastebin username|None|
|password|string|None|False|Pastebin password|None|
|key|string|None|True|API Key|None|

The scraping tasks require a [Pastebin Pro account](http://pastebin.com/api_scraping_faq).

## Troubleshooting

Scraping tasks require the IP of the machine running Komand to need be [whitelisted by Pastebin](http://pastebin.com/api_scraping_faq).

## Workflows

Examples:

* Password dumps
* Social intelligence

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - Force HTTPS connections, Pastebin will block HTTP requests beginning on March 1st, 2018
* 0.1.2 - SSL bug fix in SDK
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Python 3 conversion | Bug fix updated endpoints

## References

* [Pastebin](http://pastebin.com/)
* [Pastebin Scraping](http://pastebin.com/api_scraping_faq)
