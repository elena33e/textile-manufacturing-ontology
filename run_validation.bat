@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Running SHACL validation...
python validator.py

echo.
echo Validation complete. Press any key to exit.
pause
