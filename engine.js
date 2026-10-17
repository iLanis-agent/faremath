// Fare Math engine - transit pass honesty.
// Mirrored float-for-float by oracle.py; keep the op order identical.

function _fixed2(x) {
  var c = Math.floor(x * 100 + 0.5);
  var w = Math.floor(c / 100), r = c - w * 100;
  return w + "." + (r < 10 ? "0" + r : "" + r);
}

function _checkPrices(pass, ride) {
  if (!isFinite(pass) || pass <= 0) throw new Error("the pass price must be more than zero");
  if (!isFinite(ride) || ride <= 0) throw new Error("the ride price must be more than zero");
}

// The break-even truth: the ride where the pass starts paying.
function breakEvenTruth(pass, ride) {
  _checkPrices(pass, ride);
  var n = Math.ceil(pass / ride - 1e-9);
  return "The $" + _fixed2(pass) + " pass against $" + _fixed2(ride) +
    " rides breaks even at ride " + n + " - ride " + (n + 1) + " onward is free.";
}

// The month truth: your real rides against the pass.
function monthTruth(pass, ride, rides) {
  _checkPrices(pass, ride);
  if (!isFinite(rides) || rides < 0) throw new Error("rides must be zero or more");
  if (rides === 0) return "Zero rides is zero rides - the pass is a donation.";
  var total = rides * ride;
  var diff = total - pass;
  var rideWord = rides === 1 ? "ride" : "rides";
  var head = rides + " " + rideWord + " at $" + _fixed2(ride) + " are $" + _fixed2(total) + " - ";
  if (Math.abs(diff) < 0.005) {
    return head + "exactly the $" + _fixed2(pass) + " pass, a wash.";
  }
  if (diff > 0) {
    return head + "the $" + _fixed2(pass) + " pass saves you $" + _fixed2(diff) + ".";
  }
  return head + "the $" + _fixed2(pass) + " pass costs $" + _fixed2(-diff) + " more than the rides.";
}

// The commute truth: what your week actually adds up to.
function commuteTruth(ridesPerDay, days) {
  if (!isFinite(ridesPerDay) || ridesPerDay < 0) throw new Error("rides per day must be zero or more");
  if (!isFinite(days) || days < 1) throw new Error("days must be at least 1");
  var total = ridesPerDay * days;
  var rWord = ridesPerDay === 1 ? "ride" : "rides";
  var dWord = days === 1 ? "day" : "days";
  var tWord = total === 1 ? "ride" : "rides";
  return ridesPerDay + " " + rWord + " a day for " + days + " " + dWord + " is " + total +
    " " + tWord + " - count the vacation days honestly.";
}
