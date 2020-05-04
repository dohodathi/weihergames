<!-- measures -->


<!-- colors -->


<style>
    a.unstyled, a.unstyled:visited {
        text-decoration: none;
        color: white;
    }

    a.unstyled:hover, a.unstyled:active {
        color: #8AF;
    }

    section {
        margin: 12px 0px;

        background-color: #2f2e33;

        border: 1px solid #3a3a3a;
        border-radius: 3px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.4);
    }

    .section-header {
        display: flex;
        padding: 16px;

        border-top-left-radius: 3px;
        border-top-right-radius: 3px;
        border-bottom: 1px solid #3a3a3a;
        background-color: #272829;
    }

    /* main layout */
    #playercard {
        padding: 1px 0;
        max-width: 500px;

        color: white;
        font-family: 'Roboto', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif;
        background-color: #27282d;
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
    }

    /* details:header */
    .playerstats {
        display: flex;
        align-items: center;
        justify-content: flex-end;

        margin-bottom: 8px;
    }

    /* rank */
    .playerstats .rank {
        display: flex;
        align-items: center;
    }

    .playerstats .rank-value {
        color: white;
        font-size: 40px;
        font-weight: bold;
    }

    .playerstats .rank-label {
        display: flex;
        flex-direction: column;
        align-items: center;

        margin-left: 16px;
    }

    /* elo */
    .playerstats .elo {
        margin-right: 10%;

        display: flex;
        flex-direction: column;
        align-items: flex-end;
    }

    .playerstats .elo-value {
        color: white;

        font-size: 20px;
        font-weight: bold;
    }

    .playerstats .elo-label {
        color: #999999;

        font-size: 12px;
        font-weight: 550;
        text-transform: uppercase;
    }

    .playerstats .rank-label-world {
        color: white;

        font-size: 16px;
        font-weight: 500;
    }

    .playerstats .rank-label-rank {
        color: #999999;

        font-size: 16px;
        font-weight: 550;
        text-transform: uppercase;
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
    .stats {
        background-color: #2f2e33;
    }

    .stats-header {
        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 0 16px;
        height: 65px;
    }

    .stats-percentage {
        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 0 16px;
        height: 65px;
    }

    .stats-ratio {
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
        border: 1px solid #3a3a3a;
    }

    .gamelist-name {
        padding-top: 16px;
        padding-left: 16px;
    }

    .gamelist-item-header {
        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 16px;
        padding-bottom: 0;
    }

    .gamelist-item-header-name {
        font-size: 1.0rem;
        font-weight: 550;
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
        margin-right: 8px;
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
            <!-- elo component -->
            <div class="elo">
                <div class="elo-label">elo rating</div>
                <div class="elo-value">10000.0</div>
            </div>

            <!-- world rank component -->
            <div class="rank">
                <div class="rank-value">0</div>
                <div class="rank-label">
                    <div class="rank-label-world">World</div>
                    <div class="rank-label-rank">Rank</div>
                </div>
            </div>
        </div>

        <div class="playername">
            <img src="/images/noun_Bear_54735.png" />
            <h1>MAZL</h1>
        </div>
    </div>

    <div class="body">
        <section class="stats">
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
        </section>

        <section class="graph">
            Graph anhand letzter Spiele mit ELO Werten
        </section>

        <!-- https://stackoverflow.com/questions/9486393/jinja2-change-the-value-of-a-variable-inside-a-loop -->
        

        <div class="gamelist">
            

            <!-- handle day separators -->
            
                

            <!-- handle year separators -->
            
            <!-- update curr year and render the changed year -->
            
            <div class="gamelist-year">2011</div>
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Sunday, 03 Apr 2011</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/hit_the_line"
                            >Hit The Line</a
                        >
                    </div>

                    <div class="gamelist-item-content">
                        <div class="gamelist-item-col-1">
                            <span class="gamelist-item-vs">vs</span>

                            <!-- opponent images -->
                            
                            <img class="gamelist-item-playerimg transparent" src="/images/users_multiple.png" />
                            

                            <!-- opponent names -->
                            <span class="gamelist-item-playername">
                                
                                <a class="unstyled" href="/users/theel"
                                    >THEEL</a
                                >
                                ,&nbsp; 
                                <a class="unstyled" href="/users/doompy"
                                    >DOOMPY</a
                                >
                                 
                            </span>
                        </div>

                        <span
                            class="gamelist-item-score lose"
                        >
                            10 - 8 - 6
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/crossboccia"
                            >Crossboccia</a
                        >
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
                                
                                <a class="unstyled" href="/users/theel"
                                    >THEEL</a
                                >
                                 
                            </span>
                        </div>

                        <span
                            class="gamelist-item-score win"
                        >
                            10 - 15
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Saturday, 02 Apr 2011</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/hit_the_line"
                            >Hit The Line</a
                        >
                    </div>

                    <div class="gamelist-item-content">
                        <div class="gamelist-item-col-1">
                            <span class="gamelist-item-vs">vs</span>

                            <!-- opponent images -->
                            
                            <img class="gamelist-item-playerimg transparent" src="/images/users_multiple.png" />
                            

                            <!-- opponent names -->
                            <span class="gamelist-item-playername">
                                
                                <a class="unstyled" href="/users/theel"
                                    >THEEL</a
                                >
                                ,&nbsp; 
                                <a class="unstyled" href="/users/doompy"
                                    >DOOMPY</a
                                >
                                 
                            </span>
                        </div>

                        <span
                            class="gamelist-item-score lose"
                        >
                            8 - 10 - 7
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            
        </div>
    </div>
</div>