mkdocs build --verbose -d build
python scripts/weihergames_elo_calculator.py
python scripts/weihergames_render_templates.py
cp scripts/temp-plot.html build/plot_elo_overall.html
cp scripts/builds/player_all.html build/

