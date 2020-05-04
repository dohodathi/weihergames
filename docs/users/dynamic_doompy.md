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
            <img src="/images/vectorstock_21320352.png" />
            <h1>DOOMPY</h1>
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
            
            <div class="gamelist-year">2018</div>
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Tuesday, 15 May 2018</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/fussgolf"
                            >Fußgolf</a
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
                            class="gamelist-item-score lose"
                        >
                            1 - 6
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
                            class="gamelist-item-score lose"
                        >
                            15 - 11
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Monday, 14 May 2018</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/pool_shot"
                            >Pool Shot</a
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
                            2 - 4
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/pool_golf"
                            >Pool Golf</a
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
                            32 - 29
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/korperball"
                            >Körperball</a
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
                            1 - 2
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/prox_the_line"
                            >Prox the Line</a
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
                            13 - 15
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/lattenschiessen"
                            >Lattenschießen</a
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
                            class="gamelist-item-score lose"
                        >
                            2 - 1
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/speedminton"
                            >Speedminton</a
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
                            class="gamelist-item-score lose"
                        >
                            2 - 0
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Saturday, 12 May 2018</div>
                

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
                            14 - 16
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Friday, 11 May 2018</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/pool_shot"
                            >Pool Shot</a
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
                            class="gamelist-item-score lose"
                        >
                            2 - 1
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
            
            <!-- update curr year and render the changed year -->
            
            <div class="gamelist-year">2012</div>
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Saturday, 28 Apr 2012</div>
                

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
                            13 - 16
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Thursday, 26 Apr 2012</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/kubb"
                            >Kubb</a
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
                            class="gamelist-item-score lose"
                        >
                            14 - 0
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/kubb"
                            >Kubb</a
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
                            0 - 10
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/kubb"
                            >Kubb</a
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
                            0 - 13
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Wednesday, 25 Apr 2012</div>
                

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
                            8 - 15
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Sunday, 01 Apr 2012</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/cart_zone"
                            >Cart-Zone</a
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
                            class="gamelist-item-score lose"
                        >
                            3 - 1
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/cart_rail"
                            >Cart-Rail</a
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
                            1 - 3
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Monday, 26 Mar 2012</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/jumpergame"
                            >Jumpergame</a
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
                            16 - 18
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/weihergolf"
                            >Weihergolf</a
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
                            15 - 5
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Saturday, 24 Mar 2012</div>
                

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
                            7 - 15
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Wednesday, 21 Mar 2012</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/lattenschiessen"
                            >Lattenschießen</a
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
                            22 - 34
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/lattenschiessen"
                            >Lattenschießen</a
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
                            22 - 31
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
                            6 - 15
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

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
                            6 - 15
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
                            4 - 15
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Tuesday, 20 Mar 2012</div>
                

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
                            7 - 15
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/lattenschiessen"
                            >Lattenschießen</a
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
                            class="gamelist-item-score lose"
                        >
                            34 - 27
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Sunday, 18 Mar 2012</div>
                

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
                            class="gamelist-item-score lose"
                        >
                            15 - 8
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
                            class="gamelist-item-score lose"
                        >
                            15 - 5
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Friday, 16 Mar 2012</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/speedminton"
                            >Speedminton</a
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
                            class="gamelist-item-score lose"
                        >
                            3 - 1
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
                            class="gamelist-item-score lose"
                        >
                            15 - 9
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Sunday, 11 Mar 2012</div>
                

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
                            class="gamelist-item-score lose"
                        >
                            15 - 11
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Saturday, 10 Mar 2012</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/lattenschiessen"
                            >Lattenschießen</a
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
                            28 - 33
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/lattenschiessen"
                            >Lattenschießen</a
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
                            class="gamelist-item-score lose"
                        >
                            33 - 27
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/lattenschiessen"
                            >Lattenschießen</a
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
                            27 - 34
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/speedminton"
                            >Speedminton</a
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
                            class="gamelist-item-score lose"
                        >
                            4 - 1
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Friday, 09 Mar 2012</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/speedminton"
                            >Speedminton</a
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
                            class="gamelist-item-score lose"
                        >
                            4 - 0
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
                            9 - 15
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Thursday, 26 Jan 2012</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/speedminton"
                            >Speedminton</a
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
                            class="gamelist-item-score lose"
                        >
                            4 - 2
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
            
            <!-- update curr year and render the changed year -->
            
            <div class="gamelist-year">2011</div>
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Tuesday, 28 Jun 2011</div>
                

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
                            2 - 12
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
                            10 - 12
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Friday, 17 Jun 2011</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/sadistenspiel"
                            >Sadistenspiel</a
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
                            1 - 2
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Thursday, 16 Jun 2011</div>
                

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
                            class="gamelist-item-score lose"
                        >
                            15 - 12
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Sunday, 12 Jun 2011</div>
                

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
                            11 - 15
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/melee_boccia"
                            >Melee-Boccia</a
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
                            class="gamelist-item-score lose"
                        >
                            15 - 12
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
                            class="gamelist-item-score lose"
                        >
                            15 - 6
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

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
                                <a class="unstyled" href="/users/mazl"
                                    >MAZL</a
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
                                <a class="unstyled" href="/users/mazl"
                                    >MAZL</a
                                >
                                 
                            </span>
                        </div>

                        <span
                            class="gamelist-item-score win"
                        >
                            8 - 10 - 7
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/jumpergame"
                            >Jumpergame</a
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
                            14 - 16
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
                            7 - 15
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Sunday, 20 Mar 2011</div>
                

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
                            class="gamelist-item-score lose"
                        >
                            16 - 14
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/weihergolf_9_loch_standard"
                            >Weihergolf 9-Loch-Standard</a
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
                            0 - 6
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            

            <!-- handle day separators -->
            
                
                </section>
                

            <!-- handle year separators -->
             

            <!-- update curr day and render the changed day -->
            
            <section>
                <div class="section-header">Tuesday, 08 Mar 2011</div>
                

                <div class="gamelist-item">
                    <div class="gamelist-item-header">
                        <a
                            class="gamelist-item-header-name unstyled"
                            href="/games/weihergolf_18_loch_wurfmodus"
                            >Weihergolf 18-Loch Wurfmodus</a
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
                            12 - 13
                        </span>
                    </div>
                </div>

            <!-- end match loop -->
            
        </div>
    </div>
</div>