:::::::::::::::::::::::::::::::::::::::::::::
@echo off
if "%cd%\" EQU "%~dp0" ((start notepad++ %0)&&(exit))
cd %~dp0
title %~0
setlocal EnableDelayedExpansion
cls
:::::::::::::::::::::::::::::::::::::::::::::
::� ����� ��� ����� ��������::437	���::850	������������� (�������� I)
::852	��������� � ����������� ������ (�������� II)::855	��������� (�������)::857	��������
::860	�������������::861	����������::863	����������� (������)
::865	�������������::866	�������::869	����������� ���������
:::::::::::::::::::::::::::::::::::::::::::::

echo �������� ������� �����
chcp 1251 >nul
echo �������� ������� �����
echo.
echo �� ������ ��� ������ ������ ������
echo.
::���������� ������� �������� �� ����� ������
set NL=^& echo.
echo ������������� %NL%^
������ %NL%^
���
:::::::::::::::::::::::::::::::::::::::::::::
(TIMEOUT /T 1)&&(pause)&&(exit /b)
:::::::::::::::::::::::::::::::::::::::::::::






10.7. Internet Access
10.8. Dates and Times
10.9. Data Compression
10.10. Performance Measurement
10.11. Quality Control
10.12. Batteries Included
11. Brief Tour of the Standard Library � Part II
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