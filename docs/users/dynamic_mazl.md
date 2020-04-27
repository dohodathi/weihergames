  

<style>
    a.unstyled, a.unstyled:visited {
        text-decoration: none;
        color: white;
    }

    a.unstyled:hover, a.unstyled:active {
        color: #8AF;
    }

    /* general layout */
    #playercard {
        color: white;
        background-color: #27282d;
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;
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

        background-color: #18171d;
    }

    .header .playername h1 {
        margin: 0;
        margin-left: 110px;

        color: white;
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

    .graph {
        display: flex;
        align-items: center;
        justify-content: center;

        height: 120px;

        color: #aaa;
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

    .gamelist-item.even {
        background-color: rgba(0,0,0,0.1);
    }

    .gamelist-item-header {
        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 16px;
        padding-bottom: 0;
    }

    .gamelist-item-content {
        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 16px;

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

    .gamelist-item-playerimg.transparent {
        background-color: transparent;
    }

    .gamelist-item-playername {
        margin-left: 8px;
    }

    .gamelist-item-score  {
        font-weight: 700;
    }

    .gamelist-item-score.win {
        color: #43D181;
    }

    .gamelist-item-score.lose {
        color: #D85E40;
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
            <img src="/images/noun_Bear_54735.png" />
            <h1>MAZL</h1>
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
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/weihergolf_18_loch_wurfmodus">Weihergolf 18-Loch Wurfmodus</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        12 - 13
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/weihergolf_9_loch_standard">Weihergolf 9-Loch-Standard</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        0 - 6
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        16 - 14
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        7 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/jumpergame">Jumpergame</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        14 - 16
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/hit_the_line">Hit The Line</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <img class="gamelist-item-playerimg transparent" src="/images/users_multiple.png" />
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                            ,&nbsp; 
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                             
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        8 - 10 - 7
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                        </span>
                    </div>

                    <span class="gamelist-item-score win">
                        10 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/hit_the_line">Hit The Line</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <img class="gamelist-item-playerimg transparent" src="/images/users_multiple.png" />
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                            ,&nbsp; 
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                             
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        10 - 8 - 6
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        15 - 6
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/melee_boccia">Melee-Boccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        15 - 12
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        11 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        15 - 12
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/sadistenspiel">Sadistenspiel</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        1 - 2
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        10 - 12
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        2 - 12
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            
            <!-- update curr year and render the changed year -->
            
            <div class="gamelist-year">2012</div>
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/speedminton">Speedminton</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        4 - 2
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        10 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/speedminton">Speedminton</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        4 - 0
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        9 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/lattenschiessen">Lattenschießen</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        28 - 33
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/lattenschiessen">Lattenschießen</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        33 - 27
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/lattenschiessen">Lattenschießen</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        27 - 34
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/speedminton">Speedminton</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        4 - 1
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        15 - 11
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/speedminton">Speedminton</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        3 - 1
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        15 - 9
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        15 - 8
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        15 - 5
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        7 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/lattenschiessen">Lattenschießen</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        34 - 27
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/lattenschiessen">Lattenschießen</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        22 - 34
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/lattenschiessen">Lattenschießen</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        22 - 31
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        6 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/hit_the_line">Hit The Line</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        6 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        4 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        10 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        7 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/jumpergame">Jumpergame</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        16 - 18
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/weihergolf">Weihergolf</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        15 - 5
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/cart_zone">Cart-Zone</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        3 - 1
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/cart_rail">Cart-Rail</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        1 - 3
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        8 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/kubb">Kubb</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        14 - 0
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/kubb">Kubb</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        0 - 10
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/kubb">Kubb</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        0 - 13
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        13 - 16
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            
            <!-- update curr year and render the changed year -->
            
            <div class="gamelist-year">2018</div>
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/pool_shot">Pool Shot</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        2 - 1
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        14 - 16
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/speedminton">Speedminton</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        2 - 0
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/lattenschiessen">Lattenschießen</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        2 - 1
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/prox_the_line">Prox the Line</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        13 - 15
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/korperball">Körperball</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        1 - 2
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/pool_golf">Pool Golf</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        32 - 29
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/pool_shot">Pool Shot</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        2 - 4
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item ">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/crossboccia">Crossboccia</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        15 - 11
                    </span>
                </div>
            </div>
            

            <!-- handle year separators -->
            

            <div class="gamelist-item even">
                <div class="gamelist-item-header">
                    <div class="gamelist-item-name">
                        <a class="unstyled" href="/games/fussgolf">Fußgolf</a>
                    </div>
                </div>

                <div class="gamelist-item-content">
                    <div class="gamelist-item-col-1">
                        <span class="gamelist-item-vs">vs</span>

                        <!-- opponent images -->
                        
                        <!-- only insert images for 1v1 matches -->
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21106731.png" />
                        
                        <img class="gamelist-item-playerimg" src="/images/vectorstock_21320352.png" />
                        
                        <!-- else render a multi user image to indicate a multiplayer game -->
                        

                        <!-- opponent names -->
                        <span class="gamelist-item-playername">
                            
                            <a class="unstyled" href="/users/theel">THEEL</a>
                             
                            <a class="unstyled" href="/users/doompy">DOOMPY</a>
                            ,&nbsp; 
                        </span>
                    </div>

                    <span class="gamelist-item-score lose">
                        1 - 6
                    </span>
                </div>
            </div>
            
        </div>
    </div>
</div>