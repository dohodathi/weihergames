

<style>
    .body {
        margin: 0;
        padding: 0;

        background-color: #27282d;
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;
    }

    /* general layout */
    #playercard {
        color: white;
    }

    #playercard img {
        border-radius: 50%;
        object-fit: contain;
        vertical-align: top;
    }

    #playercard .header {
        margin: 16px;
        margin-bottom: 0px;

        background-color: transparent;
    }

    #playercard .body {
        margin: 16px;
        margin-top: 0px;

        background-color: #2f2e33;
    }

    /* details:header */
    .header .playerstats {
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }

    .header .playername {
        position: relative;
        display: flex;
        align-items: center;

        height: 68px;

        color: white;
        background-color: #18171d;
    }

    .header .playername h1 {
        margin: 0;
        margin-left: 110px;

        font-size: 24px;
        font-weight: 700;
    }

    .header .playername img {
        position: absolute;
        bottom: 34px;
        left: 16px;
        z-index: 1;

        width: 94px;
        height: 94px;

        background-color: white;
    }

    /* details:body */
    .body .stats {
    }

    .body .stats-header {
        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 0 16px;
        height: 65px;
    }

    .body .stats-percentage {
        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 0 16px;
        height: 65px;
    }

    .body .stats-ratio {
        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 0 16px;
        height: 65px;
    }

    .body .graph {
        height: 180px;

        background-color: #27282d;
        border-top: 1px solid #3a3a3a;
        border-bottom: 1px solid #3a3a3a;
    }

    /* gamelist */
    .gamelist {
    }

    .gamelist-year {
        display: flex;
        align-items: center;
        justify-content: center;

        padding: 16px;

        background-color: #18171d;
    }

    .gamelist-name {
        padding-top: 16px;
        padding-left: 16px;
    }

    .gamelist-item {
        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 0 16px;
        height: 80px;

        border-bottom: 1px solid #3a3a3a;
    }

    .gamelist-item-col-1 {
        display: flex;
        align-items: center;
    }

    .gamelist-item-vs {
        margin-right: 16px;
    }

    .gamelist-item-playerimg {
        width: 45px;
        height: 45px;

        border: 1px solid #707070;
        background-color: white;
    }

    .gamelist-item-playername {
        margin-left: 16px;
    }
</style>

<div id="playercard">
    <div class="header">
        <div class="playerstats">
            <div class="playerstats-elo">
                <div class="label">elo rating</div>
                <div class="value">10000.0</div>
            </div>

            <div class="playerstats-rank">
                <div class="value">0</div>
                <div class="label">
                    <div class="world">World</div>
                    <div class="rank">Rank</div>
                </div>
            </div>
        </div>

        <div class="playername">
            <img src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21106731.png" />
            <h1>THEEL</h1>
        </div>
    </div>

    <div class="body">
        <div class="stats">
            <div class="stats-header">
                <div>Statistics</div>
                <div>Ladder</div>
                <div>Seasons</div>
                <div>All</div>
            </div>

            <div class="stats-percentage">
                <div class="title">Win rate</div>
                <div class="value">
                    0.0%
                </div>
                <div class="value">
                    0.0%
                </div>
                <div class="value">
                    0.0%
                </div>
            </div>

            <div class="stats-ratio">
                <div class="title">Matches</div>

                <div class="value">
                    <span class="stats-ratio-win">0</span>&nbsp;/&nbsp;
                    <span class="stats-ratio-tie">0</span>&nbsp;/&nbsp;
                    <span class="stats-ratio-lose">0</span>
                </div>

                <div class="value">
                    <span class="stats-ratio-win">0</span>&nbsp;/&nbsp;
                    <span class="stats-ratio-tie">0</span>&nbsp;/&nbsp;
                    <span class="stats-ratio-lose">0</span>
                </div>

                <div class="value">
                    <span class="stats-ratio-win">0</span>&nbsp;/&nbsp;
                    <span class="stats-ratio-tie">0</span>&nbsp;/&nbsp;
                    <span class="stats-ratio-lose">0</span>
                </div>
            </div>
        </div>

        <div class="graph">
            Graph anhand letzter Spiele mit ELO Werten
        </div>

        <!-- https://stackoverflow.com/questions/9486393/jinja2-change-the-value-of-a-variable-inside-a-loop -->
        

        <div class="gamelist">
            

            <!-- handle year separators -->
            
            <!-- update curr year and render the changed year -->
            
            <div class="gamelist-year">2011</div>
            

            <div class="gamelist-name">Weihergolf 18-Loch Wurfmodus</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    12-13
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Weihergolf 9-Loch-Standard</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    0-6
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    16-14
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    7-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Jumpergame</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    14-16
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Hit The Line</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/noun_Bear_54735.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                    <span class="gamelist-item-playername">
                        MAZL&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    8-10-7
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/noun_Bear_54735.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        MAZL&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    10-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Hit The Line</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/noun_Bear_54735.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                    <span class="gamelist-item-playername">
                        MAZL&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    10-8-6
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    15-6
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Melee-Boccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    15-12
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    11-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    15-12
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Sadistenspiel</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    1-2
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    10-12
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    2-12
                </span>
            </div>
            

            <!-- handle year separators -->
            
            <!-- update curr year and render the changed year -->
            
            <div class="gamelist-year">2012</div>
            

            <div class="gamelist-name">Speedminton</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    4-2
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    10-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Speedminton</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    4-0
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    9-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Lattenschießen</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    28-33
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Lattenschießen</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    33-27
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Lattenschießen</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    27-34
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Speedminton</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    4-1
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    15-11
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Speedminton</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    3-1
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    15-9
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    15-8
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    15-5
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    7-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Lattenschießen</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    34-27
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Lattenschießen</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    22-34
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Lattenschießen</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    22-31
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    6-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Hit The Line</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    6-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    4-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    10-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    7-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Jumpergame</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    16-18
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Weihergolf</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    15-5
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Cart-Zone</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    3-1
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Cart-Rail</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    1-3
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    8-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Kubb</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    14-0
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Kubb</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    0-10
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Kubb</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    0-13
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    13-16
                </span>
            </div>
            

            <!-- handle year separators -->
            
            <!-- update curr year and render the changed year -->
            
            <div class="gamelist-year">2018</div>
            

            <div class="gamelist-name">Pool Shot</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    2-1
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    14-16
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Speedminton</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    2-0
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Lattenschießen</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    2-1
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Prox the Line</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    13-15
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Körperball</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    1-2
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Pool Golf</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    32-29
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Pool Shot</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    2-4
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Crossboccia</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    15-11
                </span>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-name">Fußgolf</div>

            <div class="gamelist-item">
                <div class="gamelist-item-col-1">
                    <span class="gamelist-item-vs">vs</span>

                    <!-- opponent images -->
                    
                    <img class="gamelist-item-playerimg" src="/Users/doompy/workspace/weihergames/scripts/../docs/images/vectorstock_21320352.png" />
                    

                    <!-- opponent names -->
                    
                    <span class="gamelist-item-playername">
                        DOOMPY&nbsp;
                    </span>
                    
                </div>

                <span class="gamelist-item-score">
                    1-6
                </span>
            </div>
            
        </div>
    </div>
</div>