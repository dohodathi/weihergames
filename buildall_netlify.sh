mkdocs build --verbose -d build
python scripts/weihergames_elo_calculator.py
python scripts/weihergames_render_templates.py
cp scripts/builds/* build/

