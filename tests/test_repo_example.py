#!/usr/bin/env python

"""Tests for `repo_example` package."""

import pytest

from click.testing import CliRunner

from repo_example import repo_example
from repo_example import cli


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    pass


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    pass


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'repo_example.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
