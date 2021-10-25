#!/bin/bash
# Note: credit to Tim Rodriguez@https://github.com/twrodriguez

install_asdf() {
    echo "Attempting to install asdf..."
    ASDF_HOME="${HOME}/.asdf"
    git_clone_or_update "https://github.com/asdf-vm/asdf.git" "${ASDF_HOME}"
    latest_tag="$(bash -c "cd \"${ASDF_HOME}\" && git describe --abbrev=0 --tags")"
    bash -c "cd \"${ASDF_HOME}\" && git checkout '${latest_tag}'"

    install_asdf_for_bash

    export ASDF_HOME
}

install_asdf_for_bash() {
    if test -f "${HOME}/.bashrc"; then
        add_activation_script_to_file "${ASDF_HOME}/asdf.sh" "{$HOME}/.bashrc"
        add_activation_script_to_file "${ASDF_HOME}/completions/asdf.bash" "{$HOME}/.bashrc"
    elif test -f "${HOME}/.bash_profile"; then
        add_activation_script_to_file "${ASDF_HOME}/asdf.sh" "{$HOME}/.bash_profile"
        add_activation_script_to_file "${ASDF_HOME}/completions/asdf.bash" "{$HOME}/.bash_profile"
    elif test -f "${HOME}/.bash_login"; then
        add_activation_script_to_file "${ASDF_HOME}/asdf.sh" "{$HOME}/.bash_login"
        add_activation_script_to_file "${ASDF_HOME}/completions/asdf.bash" "{$HOME}/.bash_login"
    fi

    add_activation_script_to_file "${ASDF_HOME}/asdf.sh" "{$HOME}/.profile"
}

add_activation_script_to_file() {
    if test -f "${2}" && ! grep -q -e "${1}" "${2}"; then
        echo "if tty; then source \"${1}\"; fi" >> "${2}"
    fi
}

git_clone_or_update() {
    if test -d "${2}/.git"; then
        bash -c "cd \"${2}\" && git pull"
    elif test -e "${2}"; then
        echo "${2} already exists and is not a valid repository!!"
        return 1
    else
        git clone "${1}" "${2}"
    fi
}

asdf_ordered_install() {
    local tool_versions_file="${1}"
    if test -z "${tool_versions_file}"; then
        tool_versions_file="${root_dir}/.tool-versions"
    fi
}

asdf_upgrade() {
  version=$(asdf list-all "$1" | grep -o "^[0-9.]\+$" | sort -V | tail -1)
  asdf install "$1" "$version"
  asdf global "$1" "$version"
}

asdf_install_latest() {
  for lang in "$@"; do
    asdf plugin-add "$lang"
    asdf_upgrade "$lang"
  done
}

asdf_add_required_plugins() {
    local tool_versions_file="${1}"
    if test -z "${tool_versions_file}"; then
        tool_versions_file="${root_dir}/.tool-versions"
    fi
    plugins=$(awk '{print $1}' < "${tool_versions_file}")
    for plugin in $plugins; do
        if ! asdf list "${plugin}" > /dev/null 2>&1; then
            asdf plugin-add "${plugin}"
        fi
    done
}


asdf_install_all_components() {
    for component in postgres mysql redis; do
        if ! asdf list ${component} > /dev/null 2>&1; then
            asdf_install_latest ${component}
        fi
    done
}
