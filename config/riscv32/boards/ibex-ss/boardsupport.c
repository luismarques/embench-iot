void
initialise_board (void)
{
}

#define MUCOUNTEREN "0x320"

void __attribute__ ((noinline, naked))
start_trigger (void)
{
  asm volatile(
    "li t0, -1\n"
    "csrw " MUCOUNTEREN ", t0\n"
    "csrw mcycle, x0\n"
    "csrw mcycleh, x0\n"
    "csrw " MUCOUNTEREN ", x0\n"
    "ret");
}

void __attribute__ ((noinline, naked))
stop_trigger (void)
{
  asm volatile(
    "li t0, -1\n"
    "csrw " MUCOUNTEREN ", t0\n"
    "ret");
}
