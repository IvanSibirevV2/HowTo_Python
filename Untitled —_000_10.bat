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