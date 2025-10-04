from edge-terminal.backend.app.services.report_builder import build_daily_micro_alpha

def test_report_build(tmp_path, monkeypatch):
    # Redirect report dir to tmp
    from edge-terminal.backend.app.services import report_builder as rb
    monkeypatch.setattr(rb, 'REPORT_ROOT', str(tmp_path))
    d = build_daily_micro_alpha()
    assert d.startswith(str(tmp_path))
