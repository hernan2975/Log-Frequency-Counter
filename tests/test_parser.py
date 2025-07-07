import pytest
from parser import parse_log

def test_parse_log_simple(tmp_path):
    log = "INFO - Inicio\nERROR - Falla\nINFO - Termino\n"
    file_path = tmp_path / "test.log"
    file_path.write_text(log)

    result = parse_log(str(file_path), ["INFO", "ERROR"])
    assert result["INFO"] == 2
    assert result["ERROR"] == 1
