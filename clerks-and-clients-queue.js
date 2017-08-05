/* 
   Simulate the following situation:
   At a post office, customers enter a single line waiting to be served by any one of two clerks.
   Every minute there is a 60% chance that a new customer arrives.
   If there is no one in line and a server is free, the customer does not wait to be served.
   When a customer is being served there is a 25% chance every minute that they complete their business and leave.
   When the clerk is free he will take the next customer in line,
   in the order that they arrived.

   Every minute, there is a 5% chance that a person standing in line will give up and leave.
   The post office is always open (24/7/365).

   Note: For simplicity you can assume customers will always arrive at the beginningof the minute
   and if they leave they do so at the end of the minute.

   a) What is the average amount of minutes a customer spends in the post office (including those not served)?
   b) What percentage of customers leave without being served?
   c) What percentage of minutes are the clerks idle?
*/
var isChanceHappen = function(percent) {
    return (percent / 100) > Math.random();
};

var isNewCustomerArrive = function() {
    return isChanceHappen(60);
};

var createClient = function(minutes) {
    return {
        createTime: minutes,
        isGiveUp: function() {
            return isChanceHappen(5);
        },
        isServed: function() {
            return isChanceHappen(25);
        }
    };
};

var createClerk = function() {
    return {
        servedClient: null,
        idleCounter: 0
    };
};

var statistics = {
    totalAmount: 0,
    giveUpAmount: 0,
    spendTime: {},
    
    saveTimeSpendInPostOffice: function(minutes) {
        this.spendTime[minutes] = 1 + (this.spendTime[minutes] || 0);
    },
    
    averageMinutesSpendInPostOffice: function() {
        var self = this;
        var xTotal = 0;
        var xSum = 0;
        Object.keys(self.spendTime).forEach(function(minutes) {
            xTotal += self.spendTime[minutes];
            xSum += self.spendTime[minutes] * minutes;
        });
        return xSum / xTotal;
    }
};

var minutes = 1;
var limit =  365 * 24 * 60; // 1 week
var queue = [];
var clerks = [createClerk(), createClerk()];

while (minutes < limit) {
    
    var i = queue.length; // is somebody give up?
    while (i--) {
        if (queue[i].isGiveUp()) {
            statistics.giveUpAmount++;
            statistics.saveTimeSpendInPostOffice(minutes - queue[i].createTime)
            queue.splice(i, 1); // remove from queue
        }
    }

    if (isNewCustomerArrive()) {
        queue.push(createClient(minutes));
        statistics.totalAmount++;
    }
    
    clerks.forEach(function(clerk) {
        if (clerk.servedClient && clerk.servedClient.isServed()) {
            statistics.saveTimeSpendInPostOffice(minutes - clerk.servedClient.createTime);
            clerk.servedClient = null;
        }
        // clerk ready to take next customer:
        if (clerk.servedClient == null) {
            if (queue.length) {
                clerk.servedClient = queue.shift();
            } else {
                clerk.idleCounter++; // clerk do nothing
            }
        }
    });
    
    minutes++; // next minute
}

console.log('', minutes, '\t', 'total period in minutes');
console.log('', queue.length, '\t\t', 'clients still in queue');
console.log('', statistics.totalAmount, '\t', 'total amount of clients');
console.log('', parseFloat(statistics.giveUpAmount/statistics.totalAmount * 100).toFixed(2),'\t\t', 'percentage of customers leave without being served');
console.log('', parseFloat(statistics.averageMinutesSpendInPostOffice()).toFixed(2), '\t\t', 'average minutes spend in post office');

// clerk statistics:
console.log('==========================');
clerks.forEach(function(clerk, index) {
    console.log('', parseFloat(clerk.idleCounter / minutes * 100).toFixed(2), '\t\t', 'percentage of idle for clerk #' + (index + 1));
});
