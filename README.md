# ansible-role-abcde

An Ansible role for the abcde CD ripping utility.

## Requirements

None.

## Role Variables

```
abcde_username: abcde
abcde_home_dir: "/home/{{ abcde_username }}"
abcde_output_dir: "{{ abcde_home_dir }}/audio"
```

## Dependencies

None.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

## License

MIT

## Author Information

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
