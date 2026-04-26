import click
from pathlib import Path
import shutil

@click.command("update-spa")
@click.option("--app", prompt="App Name")
@click.option("--name", default="frontend", prompt="SPA Name")
def update_spa(app, name):
    """Update an existing SPA with latest template configs"""
    spa_path = Path("../apps", app, name)
    
    if not spa_path.exists():
        click.echo(f"❌ SPA {name} not found in app {app}")
        return
    
    click.echo(f"🔄 Updating {app}/{name}...")
    
    # Update tailwind.config.js
    tailwind_config = spa_path / "tailwind.config.js"
    if tailwind_config.exists():
        new_config = '''/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
    './node_modules/intrakore-ui/src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
'''
        tailwind_config.write_text(new_config)
        click.echo("  ✅ Updated tailwind.config.js")
    
    # Optionally copy latest libs
    source_libs = Path(__file__).parent.parent.parent / "libs"
    target_libs = spa_path.parent.parent / "libs"
    if source_libs.exists():
        shutil.copytree(source_libs, target_libs, dirs_exist_ok=True)
        click.echo("  ✅ Updated libs folder")
    
    click.echo(f"✅ {app}/{name} updated successfully!")
