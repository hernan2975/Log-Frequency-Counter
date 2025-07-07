import click
import json
from parser import parse_log

@click.command()
@click.argument('logfile', type=click.Path(exists=True))
@click.option('--keywords', default='ERROR,WARNING,INFO', help='Niveles de log a contar')
@click.option('--top', default=3, help='Cantidad de eventos más frecuentes a mostrar')
@click.option('--export', type=click.Path(), help='Ruta para exportar resultados como JSON')
def main(logfile, keywords, top, export):
    keywords = [kw.strip().upper() for kw in keywords.split(',')]
    try:
        counts = parse_log(logfile, keywords)
        top_events = counts.most_common(top)

        click.echo("\n📊 Eventos más frecuentes:")
        for level, count in top_events:
            click.echo(f"{level}: {count}")

        if export:
            with open(export, 'w') as f:
                json.dump(dict(top_events), f, indent=2)
            click.echo(f"\n📝 Resultados exportados a: {export}")

    except Exception as e:
        click.echo(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
