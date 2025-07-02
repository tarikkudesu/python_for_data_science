
def ft_tqdm(lst: range) -> None:
    """

    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.

    """
    end = int((lst.stop - lst.start) / lst.step)
    prog = 0
    while (prog <= end):
        scaled = int((prog / end) * 100)
        fill = "".join(["█"] * scaled) + "".join(["░"] * (100 - scaled))
        print(f"\r{scaled: >3}%[{fill}] {prog}/{end} ", end="", flush=True)
        yield prog
        prog += 1
