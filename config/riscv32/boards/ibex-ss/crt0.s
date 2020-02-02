# Copyright lowRISC contributors.
# SPDX-License-Identifier: GPL-3.0-or-later

.section .vectors, "ax"

.org 0x80 # reset vector
  jal x0, _start

.section .text

.global _start
_start:
  mv gp, x0
  mv tp, x0
  la x2, _stack_start

  # clear BSS
  la t0, _bss_start
  la t1, _bss_end

  bge t0, t1, zero_loop_end

zero_loop:
  sw x0, 0(t0)
  addi t0, t0, 4
  ble t0, t1, zero_loop
zero_loop_end:

  li a0, 0
  li a1, 0
  call main

  # Halt simulation
  li t0, 0x20004 # CTRL
  li t1, 1       # stop
  sw t1, 0(t0)
