import types
from unittest import mock

import sys
import os
import importlib

dummy_ft = types.SimpleNamespace(
    SnackBar=lambda *a, **k: types.SimpleNamespace(open=False),
    Text=lambda t: t,
    colors=types.SimpleNamespace(GREEN_400="GREEN", RED_400="RED"),
    Page=type("Page", (), {}),
)

with mock.patch.dict(sys.modules, {"flet": dummy_ft}):
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    Main_1 = importlib.import_module("Main_1")


def make_dummy_page():
    page = types.SimpleNamespace()
    page.update = mock.MagicMock()
    return page


@mock.patch.object(Main_1, "datetime")
@mock.patch.object(Main_1, "open", new_callable=mock.mock_open)
@mock.patch.object(Main_1.os.path, "exists", return_value=False)
@mock.patch.object(Main_1.os, "makedirs")
def test_create_directory_and_write_file(mock_makedirs, mock_exists, mock_open, mock_datetime):
    page = make_dummy_page()
    interrogatorio = {"Sec": {"K": "V", "Ignore": ""}}

    mock_datetime.now.return_value.strftime.return_value = "20230101_000000"

    dummy_ft = types.SimpleNamespace(
        SnackBar=lambda *a, **k: types.SimpleNamespace(open=False),
        Text=lambda t: t,
        colors=types.SimpleNamespace(GREEN_400="GREEN", RED_400="RED"),
    )

    with mock.patch.object(Main_1, "ft", dummy_ft):
        Main_1.save_interrogatorio_to_txt(interrogatorio, page)

    mock_exists.assert_called_once_with("dados_interrogatorio")
    mock_makedirs.assert_called_once_with("dados_interrogatorio")
    mock_open.assert_called_once_with(
        "dados_interrogatorio/interrogatorio_mtc_20230101_000000.txt",
        "w",
        encoding="utf-8",
    )
    handle = mock_open()
    handle.write.assert_any_call("\nSec\n")
    handle.write.assert_any_call("=" * 50 + "\n")
    handle.write.assert_any_call("K: V\n")
    assert page.snack_bar.open is True
    page.update.assert_called_once()


@mock.patch.object(Main_1, "datetime")
@mock.patch.object(Main_1, "open", new_callable=mock.mock_open)
@mock.patch.object(Main_1.os.path, "exists", return_value=True)
@mock.patch.object(Main_1.os, "makedirs")
def test_existing_directory_no_makedirs(mock_makedirs, mock_exists, mock_open, mock_datetime):
    page = make_dummy_page()
    interrogatorio = {"Sec": {}}

    mock_datetime.now.return_value.strftime.return_value = "20230101_000000"

    dummy_ft = types.SimpleNamespace(
        SnackBar=lambda *a, **k: types.SimpleNamespace(open=False),
        Text=lambda t: t,
        colors=types.SimpleNamespace(GREEN_400="GREEN", RED_400="RED"),
    )

    with mock.patch.object(Main_1, "ft", dummy_ft):
        Main_1.save_interrogatorio_to_txt(interrogatorio, page)

    mock_exists.assert_called_once_with("dados_interrogatorio")
    mock_makedirs.assert_not_called()
    mock_open.assert_called_once()
    assert page.snack_bar.open is True
    page.update.assert_called_once()
