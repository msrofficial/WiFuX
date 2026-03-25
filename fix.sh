#!/bin/bash

B="\e[1m"
R="\e[0m"
C_B_GRN="\e[1;32m"
C_D_GRN="\e[0;32m"
C_B_YLW="\e[1;33m"

trap 'echo -e "\n${C_B_YLW}[ ! ] Script interrupted. Exiting...${R}"; kill 0; exit 1' SIGINT

clear
echo -e "${C_B_GRN}${B}"
echo "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰"
echo "        F I X   T E R M U X   R O O T          "
echo "           Powered by: msrofficial            "
echo "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰"
echo -e "${R}"

success() { echo -e "${C_B_GRN}[ ✔ ]${R} ${C_D_GRN}${1}${R}"; }
warn() { echo -e "${C_B_YLW}[ ! ]${R} ${C_B_YLW}${1}${R}"; }
error() { echo -e "${C_B_YLW}[ ✘ ]${R} ${C_B_YLW}${1}${R}"; }

run_with_spinner() {
  local msg="$1"
  shift
  "$@" > /dev/null 2>&1 &
  local pid=$!
  local spinstr='⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
  
  while kill -0 $pid 2>/dev/null; do
    for i in $(seq 0 9); do
      echo -ne "\r${C_B_GRN}[ ${spinstr:$i:1} ]${R} ${C_B_YLW}${msg}...${R}"
      sleep 0.1
    done
  done
  
  wait $pid
  local status=$?
  echo -ne "\r\033[K" 
  return $status
}

if run_with_spinner "Purging conflicting binaries (tsu)" pkg uninstall tsu -y; then
  success "tsu completely removed from system."
else
  warn "No conflicting tsu found. Bypassing."
fi

if run_with_spinner "Syncing repositories & upgrading core" bash -c "pkg update -y && pkg upgrade -y"; then
  success "Core packages are up to date."
else
  warn "Minor sync issues detected, continuing operation."
fi

if run_with_spinner "Injecting 'sudo' environment" pkg install sudo -y; then
  success "Sudo framework successfully injected."
else
  error "Sudo installation failed. Manual intervention required."
fi

echo -e "\n${C_B_GRN}[ * ]${R} ${C_B_YLW}Initiating Root Matrix Scan...${R}"

SU_PATHS=(
  /system/bin/su
  /debug_ramdisk/su
  /system/xbin/su
  /sbin/su
  /sbin/bin/su
  /system/sbin/su
  /su/xbin/su
  /su/bin/su
  /magisk/.core/bin/su
  /system/product/bin/su
)

root_matrix() {
  if [ "$(id -u 2>/dev/null)" = "0" ]; then
    success "System is already running as ROOT (uid 0)."
    return 0
  fi

  if command -v sudo >/dev/null 2>&1 && sudo -n true 2>/dev/null; then
    whoami_out="$(sudo whoami 2>/dev/null || true)"
    success "Sudo access granted. Identity: ${whoami_out}"
    return 0
  fi

  echo -e "${C_B_GRN}      Scanning known root directories...${R}"
  sleep 0.5 
  
  for path in "${SU_PATHS[@]}"; do
    if [ -x "$path" ]; then
      echo -e "${C_B_YLW}      Target acquired: ${path}${R}"
      if "$path" -c "id -u" >/dev/null 2>&1; then
        success "Valid root binary verified at: ${path}"
        echo ""
        echo -ne "${C_B_GRN}[?] Initialize root terminal now? [y/N]: ${R}"
        read ans
        ans="${ans:-n}"
        if [[ "$ans" =~ ^[Yy]$ ]]; then
          echo -e "${C_B_GRN}Entering root matrix...${R}"
          exec "$path" -c "sh"
        else
          echo -e "${C_B_YLW}[ * ]${R} ${C_D_GRN}Aborted. Use '${path} -c sh' to launch manually later.${R}"
        fi
        return 0
      fi
    fi
  done

  error "Root binary not found in matrix."
  warn "Verify if Magisk/KernelSU is actively running."
  return 1
}

root_matrix
echo ""

echo -e "${C_B_GRN}▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰${R}"
echo -e "${B}${C_B_YLW}  PROTOCOL COMPLETE. MAINTAINER: MSR Sakibur${R}"
echo -e "${C_D_GRN}  [*] GitHub       : ${C_B_GRN}msrofficial${R}"
echo -e "${C_D_GRN}  [*] Facebook     : ${C_B_GRN}sakibur.msr${R}"
echo -e "${C_D_GRN}  [*] Telegram     : ${C_B_GRN}@msr0official${R}"
echo -e "${C_D_GRN}  [*] TG Channel   : ${C_B_GRN}@msrpatch${R}"
echo -e "${C_D_GRN}  [*] Google Search: ${C_B_GRN}msr sakibur${R}"
echo -e "${C_B_GRN}▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰${R}"
