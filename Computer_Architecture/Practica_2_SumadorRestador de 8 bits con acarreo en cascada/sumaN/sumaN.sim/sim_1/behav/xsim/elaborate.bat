@echo off
REM ****************************************************************************
REM Vivado (TM) v2019.1 (64-bit)
REM
REM Filename    : elaborate.bat
REM Simulator   : Xilinx Vivado Simulator
REM Description : Script for elaborating the compiled design
REM
REM Generated by Vivado on Mon Mar 02 13:11:05 -0600 2020
REM SW Build 2552052 on Fri May 24 14:49:42 MDT 2019
REM
REM Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
REM
REM usage: elaborate.bat
REM
REM ****************************************************************************
echo "xelab -wto dcd70c18997c4d11ae2ba7070f9a9953 --incr --debug typical --relax --mt 2 -L xil_defaultlib -L secureip --snapshot sumaNtb_behav xil_defaultlib.sumaNtb -log elaborate.log"
call xelab  -wto dcd70c18997c4d11ae2ba7070f9a9953 --incr --debug typical --relax --mt 2 -L xil_defaultlib -L secureip --snapshot sumaNtb_behav xil_defaultlib.sumaNtb -log elaborate.log
if "%errorlevel%"=="0" goto SUCCESS
if "%errorlevel%"=="1" goto END
:END
exit 1
:SUCCESS
exit 0
