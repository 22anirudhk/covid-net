function createCard(state) {
    var card = document.createElement("div");
    card.id = state + "-card";
    card.className = "card";
     
        var caseInfoDiv = document.createElement("div");
        caseInfoDiv.id = state + "case-info";
        caseInfoDiv.className = "case-info";
            var stateName = document.createElement("h2");
            stateName.innerHTML = state;
    
            var tomorrow = document.createElement("h3");
            tomorrow.innerHTML = "Tomorrow";
            tomorrow.className = "case-info-heading";
            var tomorrowCases = document.createElement("h4");
    
            var threeDays = document.createElement("h3");
            var threeCases = document.createElement("h4");
            threeDays.innerHTML = "Three Days";
            threeDays.className = "case-info-heading";
    
            var week = document.createElement("h3");
            var weekCases = document.createElement("h4");
            week.innerHTML = "One Week";
            week.className = "case-info-heading";
            
        
        caseInfoDiv.appendChild(stateName);
        caseInfoDiv.appendChild(tomorrow);
        caseInfoDiv.appendChild(tomorrowCases);
        caseInfoDiv.appendChild(threeDays);
        caseInfoDiv.appendChild(threeCases);
        caseInfoDiv.appendChild(week);
        caseInfoDiv.appendChild(weekCases);
        
        var graphDiv = document.createElement("div");
        graphDiv.id = state + "graph-div";
        graphDiv.className = "graph-div";
    card.appendChild(caseInfoDiv);
    card.appendChild(graphDiv);
    
    document.getElementById("content").appendChild(card);
}

//createCard("California");
