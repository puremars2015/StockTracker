function GetPageRowHTML(n) {
    let templete = `<div id="row${n}" class="row">
                        <div class="left-panel">
                            <label>Stock Monitor:${n+1}</label>
                            <div class="chart-display">
                                <canvas id="chart${n}" height="400px" width="350px"></canvas>
                            </div>
                            <div class="control-panel">
                                <div>
                                    <button id="qbtn${n}" class="finger" onclick="Query(this)" value="${n}">查詢個股資料</button>
                                    <!-- input id="no${n}" type="text" value="${n}"  hidden -->
                                </div>
                                <div>
                                    <label class="lb">個股代號(例如:台積電2330):</label>
                                    <input id="qsc${n}" class="condition" type="text" placeholder="ex:2330">
                                </div>
                                <div>
                                    <label class="lb">查詢區間(例如:由今天開始向前一個月,輸入1mo):</label>
                                    <div style="margin-bottom:10px">
                                        <button name="period${n}" class="finger" value="${n}" onclick="ChangePeriod(this)">1d</button>
                                        <button name="period${n}" class="finger" value="${n}" onclick="ChangePeriod(this)">5d</button>
                                        <button name="period${n}" class="finger" value="${n}" onclick="ChangePeriod(this)">1mo</button>
                                    </div>
                                    <div style="margin-bottom:10px">
                                        <input type="text "id="qd${n}" class="condition" type="text" value="1mo" readonly>
                                    </div>
                                  
                                </div>          
                                <div>
                                    <label class="lb">模糊化係數(例如:30,表示以30為一格,減少小波動):</label>
                                    <input id="mp${n}" class="condition" type="text" placeholder="ex:30">
                                </div>
                            </div>
                        </div>
                        <div id="rpanel${n}" class="right-panel">

                        </div>
                    </div>`;

    return templete;
}