import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages_installed(Package):
    packages = [
        'abcde',
        'cd-discid',
        'flac',
        'icedax'
    ]

    for package in packages:
        assert Package(package).is_installed


def test_abcde_user_present(User):
    assert User('abcde').name == 'abcde'


def test_abcde_output_dir_present(File):
    output_dir = File('/home/abcde/audio')

    assert output_dir.exists
    assert output_dir.is_directory
    assert output_dir.user == 'abcde'
    assert output_dir.mode == 0o755


def test_abcde_conf_present(File):
    assert File('/home/abcde/.abcde.conf').exists


def test_abcded_script_present(File):
    assert File('/usr/local/bin/abcded').exists


def test_discready_script_present(File):
    assert File('/usr/local/bin/discready').exists


def test_abcde_service_file_present(File):
    assert File('/etc/systemd/system/abcde.service').exists


def test_abcde_service_started(Service):
    assert Service('abcde').is_running
