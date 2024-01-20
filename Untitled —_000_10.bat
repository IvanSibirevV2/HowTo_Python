:::::::::::::::::::::::::::::::::::::::::::::
@echo off
if "%cd%\" EQU "%~dp0" ((start notepad++ %0)&&(exit))
cd %~dp0
title %~0
setlocal EnableDelayedExpansion
cls
:::::::::::::::::::::::::::::::::::::::::::::
::В общем оно вроде работает::437	США::850	Многоязыковый (латиница I)
::852	Восточная и центральная Европа (латиница II)::855	Кириллица (русский)::857	Турецкий
::860	Португальский::861	Исландский::863	Французский (Канада)
::865	Скандинавский::866	Русский::869	Современный греческий
:::::::::::::::::::::::::::::::::::::::::::::

echo Включаем русский текст
chcp 1251 >nul
echo Включаем русский текст
echo.
echo мы только что вывели пустую строку
echo.
::переменная символа перехода на новую строку
set NL=^& echo.
echo Многострочный %NL%^
Привет %NL%^
Мир
:::::::::::::::::::::::::::::::::::::::::::::
(TIMEOUT /T 1)&&(pause)&&(exit /b)
:::::::::::::::::::::::::::::::::::::::::::::






7.1.3. Manual String Formatting
7.1.4. Old string formatting
7.2. Reading and Writing Files
7.2.1. Methods of File Objects
7.2.2. Saving structured data with json
8. Errors and Exceptions
8.1. Syntax Errors
8.2. Exceptions
8.3. Handling Exceptions
8.4. Raising Exceptions
8.5. Exception Chaining
8.6. User-defined Exceptions
8.7. Defining Clean-up Actions
8.8. Predefined Clean-up Actions
8.9. Raising and Handling Multiple Unrelated Exceptions
8.10. Enriching Exceptions with Notes
9. Classes
9.1. A Word About Names and Objects
9.2. Python Scopes and Namespaces
9.2.1. Scopes and Namespaces Example
9.3. A First Look at Classes
9.3.1. Class Definition Syntax
9.3.2. Class Objects
9.3.3. Instance Objects
9.3.4. Method Objects
9.3.5. Class and Instance Variables
9.4. Random Remarks
9.5. Inheritance
9.5.1. Multiple Inheritance
9.6. Private Variables
9.7. Odds and Ends
9.8. Iterators
9.9. Generators
9.10. Generator Expressions
10. Brief Tour of the Standard Library
10.1. Operating System Interface
10.2. File Wildcards
10.3. Command Line Arguments
10.4. Error Output Redirection and Program Termination
10.5. String Pattern Matching
10.6. Mathematics
10.7. Internet Access
10.8. Dates and Times
10.9. Data Compression
10.10. Performance Measurement
10.11. Quality Control
10.12. Batteries Included
11. Brief Tour of the Standard Library — Part II
11.1. Output Formatting
11.2. Templating
11.3. Working with Binary Data Record Layouts
11.4. Multi-threading
11.5. Logging
11.6. Weak References
11.7. Tools for Working with Lists
11.8. Decimal Floating Point Arithmetic
12. Virtual Environments and Packages
12.1. Introduction
12.2. Creating Virtual Environments
12.3. Managing Packages with pip
13. What Now?
14. Interactive Input Editing and History Substitution
14.1. Tab Completion and History Editing
14.2. Alternatives to the Interactive Interpreter
15. Floating Point Arithmetic: Issues and Limitations
15.1. Representation Error
16. Appendix
16.1. Interactive Mode
16.1.1. Error Handling
16.1.2. Executable Python Scripts
16.1.3. The Interactive Startup File
16.1.4. The Customization Modules