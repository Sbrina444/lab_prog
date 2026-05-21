import typer

from lab_package import lab4, lab5, lab6

app = typer.Typer(help="Утилита для запуска лабораторных работ 4-6")



@app.command()
def lab4_run():


    lab4.to_str([1, [2, [3, [4, [5]]]]])
    lab4.to_str([1, [2, [3, [4, [5]]]]])
    lab4.a(5)
    lab4.a(5)


@app.command()
def lab4_to_str_iterative(
        lst_str: str = typer.Argument("[1, [2, [3, [4, [5]]]]]", help="Список в формате Python")
):

    import ast
    lst = ast.literal_eval(lst_str)
    result = lab4.to_str(lst)
    typer.echo(result)


@app.command()
def lab4_sequence_iterative(
        n: int = typer.Argument(5, help="Номер элемента")
):

    result = lab4.a(n)
    typer.echo(f"a({n}) = {result}")


@app.command()
def lab5_run(
        max_calls: int = typer.Option(5, "--max-calls", "-m", help="Максимальное количество вызовов"),
        values: str = typer.Option("1,2,2,3,1,4,5", "--values", "-v", help="Значения через запятую")
):


    def limit_calls_custom(max_calls):
        def decorator(func):
            count = 0

            def wrapper(value):
                nonlocal count
                if count >= max_calls:
                    print("Стоп: слишком много вызовов")
                    return None
                count += 1
                return func(value)

            return wrapper

        return decorator

    seen = []

    @limit_calls_custom(max_calls)
    def inner(value):
        if value not in seen:
            seen.append(value)
            return value
        return None

    data = [int(x.strip()) for x in values.split(',')]

    typer.echo(f"Данные: {data}")
    typer.echo(f"Лимит вызовов: {max_calls}")
    typer.echo("Результат:")

    for x in data:
        result = inner(x)
        if result is not None:
            typer.echo(f"  {result}")


@app.command()
def lab5_run_original():

    exec(open("lab_package/lab5.py").read())



@app.command()
def lab6_run(
        colors: str = typer.Option("red,blue", "--colors", "-c", help="Цвета через запятую"),
        sizes: str = typer.Option("S,M", "--sizes", "-s", help="Размеры через запятую"),
        materials: str = typer.Option("cotton,polyester", "--materials", "-m", help="Материалы через запятую")
):

    from itertools import product

    colors_list = [c.strip() for c in colors.split(',')]
    sizes_list = [s.strip() for s in sizes.split(',')]
    materials_list = [m.strip() for m in materials.split(',')]

    typer.echo(f"Цвета: {colors_list}")
    typer.echo(f"Размеры: {sizes_list}")
    typer.echo(f"Материалы: {materials_list}")
    typer.echo("Комбинации:")

    for combo in product(colors_list, sizes_list, materials_list):
        typer.echo(f"  {combo}")


@app.command()
def lab6_run_original():

    exec(open("lab_package/lab6.py").read())



@app.command()
def run_all():
    typer.echo("\n=== Запуск lab4 ===")
    lab4_run()

    typer.echo("\n=== Запуск lab5 ===")
    lab5_run_original()

    typer.echo("\n=== Запуск lab6 ===")
    lab6_run_original()


