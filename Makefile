CC = python3
WIN = windows
LIN = linux
SCRIPT = rabbit_chase.py
WIN_EXE = --onefile $(SCRIPT) --distpath $(WIN) --workpath $(WIN) --specpath $(WIN) --clean
LIN_EXE = --onefile $(SCRIPT) --distpath $(LIN) --workpath $(LIN) --specpath $(LIN) --clean


windows:
	mkdir $(WIN)
	pip install pyinstaller
	pyinstaller $(WIN_EXE)
	./$(WIN)/rabbit_chase.exe

linux:
	mkdir $(LIN)
	pip install pyinstaller
	pyinstaller $(LIN_EXE)
	./$(LIN)/rabbit_chase.exe

web:
	cmd /c start http://localhost:5000/
	python app.py

clean:
	rm -rf $(WIN)
	rm -rf $(LIN)
