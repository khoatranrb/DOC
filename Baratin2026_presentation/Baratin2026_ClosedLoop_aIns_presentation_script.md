# Presentation script: Baratin et al. (2026), *Closed-loop readout of anterior insula high-gamma activity steers value-based decisions*

*Nature Communications*, 2026 · doi:10.1038/s41467-026-75265-5

**17 slides · approx. 22 minutes.** The same text is in the speaker notes of each slide in the .pptx.

## Before you present: pronunciation and plain meanings

| Term | Say it as | Plain meaning |
|---|---|---|
| Anterior insula (aIns) | "an-TEER-ee-er IN-syoo-luh" | Brain region tied to unpleasant things: losses, pain, bad mood |
| vmPFC | "V-M-P-F-C" (ventromedial prefrontal cortex) | Brain region that computes how much we value things |
| sEEG | "S-E-E-G" (stereo-electroencephalography) | Electrodes implanted inside the brain of epilepsy patients |
| Broadband gamma activity (BGA) | "broadband GAM-uh" | Fast brain waves (70–150 Hz): a local "activity meter" |
| Interictal | "in-ter-IK-tal" | Abnormal epileptic spikes between seizures |
| Theta | "THAY-tuh" | A slower brain rhythm (4–8 Hz) |
| MAD | "M-A-D" (median absolute deviation) | A robust measure of spread, like standard deviation |
| β | "beta" | A regression coefficient (size and direction of an effect) |

## Slide overview

| # | Slide | Time |
|---|---|---|
| 1 | Title | ~0.75 min |
| 2 | Why do we decide differently when facing the same offer? | ~1.5 min |
| 3 | Recording from inside the brain | ~1.25 min |
| 4 | Terms used in this talk | ~1.5 min |
| 5 | The idea: let the brain decide when the offer appears | ~1.25 min |
| 6 | Participants and tasks | ~1.5 min |
| 7 | The closed-loop brain-computer interface | ~1.5 min |
| 8 | Detecting up- and down-states; controlling difficulty | ~1.5 min |
| 9 | Sanity check: choices follow the value of the offer | ~1 min |
| 10 | Main result: insula up-states make people accept more | ~1.5 min |
| 11 | Insula activity: high before the offer, suppressed after | ~1.5 min |
| 12 | Which moment predicts the choice? | ~1.25 min |
| 13 | vmPFC: same brain pattern, no effect on choices | ~1.25 min |
| 14 | Proposed mechanism and supporting evidence | ~1.25 min |
| 15 | Strengths and weaknesses: how causal is this evidence? | ~2 min |
| 16 | Take-home messages | ~1 min |
| 17 | Thank you | ~0.25 min |

---

## Slide 1: Title  _(~0.75 min)_

Hello everyone. Today I'll present a 2026 Nature Communications paper by Clarissa Baratin, Julien Bastin and colleagues from Grenoble and the Paris Brain Institute. The title is "Closed-loop readout of anterior insula high-gamma activity steers value-based decisions".

In plain words, the authors built a system that watches brain activity live and shows a person a decision at exactly the moment a particular brain region is unusually active, or unusually quiet. They then check whether that moment changes the person's answer.

The short answer is yes, for one brain region. The brain's spontaneous state when an offer appears can tip the decision one way or the other.

## Slide 2: Why do we decide differently when facing the same offer?  _(~1.5 min)_

Let's start with a simple observation. If you get exactly the same offer twice, you won't always give the same answer. Classic decision models treat that inconsistency as random noise.

But a growing body of research suggests part of this "noise" comes from the brain itself. Brain activity is never still. It constantly rises and falls on its own, even when nothing is happening. Several studies show that the level of activity just before an option appears can predict what a person will perceive or choose.

Two brain regions matter here. The first is the vmPFC, short for ventromedial prefrontal cortex, a region just behind the forehead that computes how much we value things. Earlier work found that when it was more active before a choice, people took more risks, as if they focused on possible gains. The second is the anterior insula, a region deep inside the side of the brain linked to unpleasant things like losses, pain and disgust. When it was more active, people were more sensitive to losses.

The problem, shown in the dark box, is that all of this evidence is correlational. Researchers recorded everything, then sorted the trials afterwards. Nobody could deliberately show an offer at the moment a region was in a particular state. So we couldn't be sure the brain state itself shapes the decision. This paper fills that gap.

## Slide 3: Recording from inside the brain  _(~1.25 min)_

Before the method, here's where the data comes from, since it's unusual.

The participants are twelve patients with severe epilepsy that medication can't control. To plan surgery, doctors implant thin electrodes directly into their brains for a week or two to find where seizures start. This is called stereo-EEG, or sEEG. While the electrodes are in, patients can volunteer for research. That gives scientists a rare chance to record directly from deep brain regions with millisecond precision, which is impossible from outside the skull.

The brain image shows every recording point used in the study: red dots in the anterior insula and green in the vmPFC.

The signal they track is called broadband gamma activity, or BGA. It's the fast part of the brain signal, between 70 and 150 cycles per second. You can think of it as a local activity meter: more BGA means more nearby neurons are firing. I'll say "gamma activity" or "activity" for short.

The two regions are the vmPFC, the "how much do I want this" region, and the anterior insula, the "this is unpleasant" region.

## Slide 4: Terms used in this talk  _(~1.5 min)_

A few terms will come up repeatedly, so here they are in plain language. I'll go through them quickly.

On the left are the task and method terms. A closed-loop brain-computer interface, or BCI, is software that reads brain signals live and reacts to them. Here it decides when to show the next offer, a bit like an event-driven trigger in code. An up-state or down-state is a short moment when activity is unusually high or low compared with the recent past. Decision value is simply the pleasant rating minus the unpleasant rating of an offer: the higher it is, the better the deal. The indifference point is the decision value where someone says yes half the time, so those are the hardest choices. A time-frequency map is a spectrogram-style heat map showing signal strength at each frequency over time. And interictal activity means abnormal epileptic spikes between seizures. They could fake an "up-state", so they're checked and removed.

On the right are the statistics terms. A mixed-effects regression is a regression over all trials from all people that lets each person have their own baseline. Logistic regression predicts the probability of a yes-or-no outcome, here accept versus reject. Beta is the fitted coefficient: its sign gives the direction of an effect and its size the strength. The p-value is roughly how likely we'd see an effect this big if there were really none, and below 0.05 is called significant. The z or t statistic is the effect divided by its uncertainty, and anything beyond about 2 is usually significant. Finally, median and MAD, or median absolute deviation, are robust versions of the mean and standard deviation that outliers don't skew.

## Slide 5: The idea: let the brain decide when the offer appears  _(~1.25 min)_

So here's the core idea. Instead of showing offers at fixed times and sorting trials afterwards, the brain decides when each offer appears.

The five steps run left to right. The system streams the electrode signal live, recomputes gamma activity every 30 milliseconds, and checks it against a threshold. When activity spikes unusually high, an up-state, or dips unusually low, a down-state, the offer appears on screen immediately. The person then accepts or rejects it.

What I like about this design is that the task and the offers stay the same. The only thing that differs between the two conditions is the brain state at the moment the offer appears.

The researchers expected the two regions to push decisions in opposite directions. Based on the earlier work, a vmPFC up-state should make the pleasant part of the offer feel more important, so people would accept more. An insula up-state should make the unpleasant part feel more important, so people would accept less. As we'll see, the insula result actually goes the other way.

## Slide 6: Participants and tasks  _(~1.5 min)_

Now the concrete setup. There were twelve patients, average age about 34, five of them women. Seven sessions were driven by the insula and eight by the vmPFC. Patients with electrodes in both regions did one session for each.

There were two tasks. The first was an offline rating task. Participants read 240 short imagined scenarios, half pleasant, like "eating a piece of birthday cake", and half unpleasant, like "stumbling in public". They rated how much they would like or dislike each one on a slider. That gives a personal score for every item.

The second was the live accept-or-reject task. Each offer combines one pleasant and one unpleasant item. For example: "Would you accept losing your house keys in exchange for going on holiday?", yes or no. The scores from the first task tell us how good each deal is for that person. That's the decision value from the glossary.

Two details matter. First, the fixation cross before each offer has no fixed duration. It stays on screen until the system detects the target brain state. Second, participants were not told that their brain activity was controlling the timing.

## Slide 7: The closed-loop brain-computer interface  _(~1.5 min)_

This is Figure 1a, the heart of the method. On the left, the signal comes from the hospital's recording system. The trace at the top is the live gamma activity, in black. The red line is the "up" threshold, the grey dashed line is the running median, and the blue line is the "down" threshold. Each small arrow marks a detection. Underneath, you can see how detections trigger trials: wait, trial 1 on an up-state, wait, trial 2 on a down-state, and so on. The offer then appears on screen and the patient answers with a game controller.

On the right is the data pipeline, which should feel familiar to anyone who has built a streaming system. The hospital amplifier samples at 512 Hz and streams over TCP/IP. An open-source tool called BCI2000 receives the stream and writes it into a buffer that MATLAB reads. Each electrode signal has its neighbour's signal subtracted, which removes noise coming from far away. Then every 30 milliseconds the code takes the last second of data, runs a Fast Fourier Transform, and adds up the power between 70 and 150 Hz. That gives the gamma activity value. It's averaged across channels, smoothed over half a second, and compared with the thresholds. If a threshold is crossed, the offer is shown. If nothing happens within 30 seconds, the offer is shown anyway, as a timeout.

## Slide 8: Detecting up- and down-states; controlling difficulty  _(~1.5 min)_

How does the system decide what counts as "unusually high" or "unusually low"? Brain signals drift over a session, so a fixed threshold wouldn't work.

They use a rolling outlier detector, similar to anomaly detection on streaming data. Over a sliding 20-second window, they compute the median of the activity and its spread using MAD, which is a robust version of standard deviation. A point more than 3.5 times that spread above the median is an up-state. A point that far below is a down-state. The spread is computed separately above and below the median, because brain activity isn't symmetric. Detected spikes only get a weight of 0.8 when the statistics are updated, so one big spike can't throw off the threshold. The practical benefit is that there's no calibration phase: the thresholds adapt on their own.

Now the trial design. Each session had 35 up-state and 35 down-state trials, strictly alternating. At least 70% of offers were designed to be hard, meaning close to each person's 50/50 point. A pilot study with healthy volunteers found that the pleasant item needs to score about 15 points higher than the unpleasant one for people to say yes half the time. The reasoning is that when a choice is obvious, the brain state won't change it. When it's a coin flip, a small internal nudge can tip the balance.

## Slide 9: Sanity check: choices follow the value of the offer  _(~1 min)_

Before looking at the brain effect, the authors check that people behaved sensibly, and they did.

On the left is Figure 1d. The horizontal axis is decision value, meaning how good the deal is, and the vertical axis is the probability of saying yes. The black curve is the average fit and the grey curves are individual people. It's a clean S-shaped curve: the better the deal, the more likely people accept. The statistics are very strong, with a z of about 17.

People took about 8 seconds per choice, which makes sense since they have to imagine two scenarios. And harder choices took a bit longer.

The most important point is in the green box. Up-state and down-state trials had the same difficulty and the same response times. So if we see a difference in choices between the two states, it can't be because one condition simply had easier offers.

## Slide 10: Main result: insula up-states make people accept more  _(~1.5 min)_

Here's the main result. When the insula drove the system, offers shown during up-states were accepted more often than offers shown during down-states.

On the left is Figure 2b, the acceptance rate for up versus down trials. Each line is one participant, and most lines slope downwards from up to down. The regression, which accounts for how good each deal was and the time between trials, gives a positive effect: beta 0.44, p = 0.04. So the effect is statistically significant.

These are epilepsy patients, so there's an obvious concern: abnormal epileptic spikes could look like "up-states" to the system. The authors detected those events, checked them by hand, and removed the affected trials. The effect held and even got slightly stronger: beta 0.47, p = 0.014.

Now recall the expectation. Since the insula is the "unpleasant" region, you'd expect high insula activity to make people accept less. The result is the opposite. The next two slides explain why.

## Slide 11: Insula activity: high before the offer, suppressed after  _(~1.5 min)_

To understand the surprise, the authors looked at what the insula did after the offer appeared.

The left panel, Figure 2c, is a spectrogram-style map showing up-state trials minus down-state trials. Red means more power in up-state trials and blue means less. Before time zero it's red, as expected, since that's how the trials were selected. After the offer, blue patches appear at the higher frequencies.

The middle panel, 2d, makes it clearer. The red line is up-state trials and the blue line is down-state trials. The red line peaks when the offer appears, by design, then drops below baseline and stays low during the grey window, about 2.5 to 4.5 seconds after the offer. The blue line does the opposite and rises. So the lines cross: high before means low after, and low before means high after.

The right panel, 2e, shows the gap between up and down for each participant. It's positive before the offer and negative after, for every single person. The statistics are extremely strong, with a p-value around 10 to the minus 20.

One important check: this flip doesn't happen during the pauses between trials. Without an offer, high moments stay higher than low moments. That means the flip isn't just a statistical artefact where extreme values naturally drift back to average. It happens because the person is processing an offer.

## Slide 12: Which moment predicts the choice?  _(~1.25 min)_

So there are two candidate signals: activity before the offer and activity after it. Which one actually relates to the yes-or-no answer, trial by trial?

For each trial, the authors took the peak activity in one of three time windows and asked whether it predicts the answer, after accounting for how good the deal was.

Activity before the offer, which is what the system used to trigger trials, did not predict the answer on a trial-by-trial basis: p = 0.20, not significant. Activity in the last second before the button press didn't either. But activity after the offer did, shown by the red card: p = 0.03. The lower the insula activity after the offer, the more likely people were to say yes.

This held for easy and hard offers alike. A slower brain rhythm, called theta, showed a similar pattern.

So the story is this. A high state before the offer leads to lower activity after it, and that lower activity is what nudges people towards accepting. The state before the offer doesn't act directly. It changes how the insula reacts to the offer.

## Slide 13: vmPFC: same brain pattern, no effect on choices  _(~1.25 min)_

Now the second region, the vmPFC. When the vmPFC drove the system, up versus down states made no difference to choices: p = 0.89. In the left panel, the participants' lines go both ways. Some accepted more in up-states and some accepted less.

You might think the system simply failed to capture anything meaningful in the vmPFC. But the middle and right panels show the same flip we saw in the insula: high before the offer, low after, and vice versa. It's just as strong statistically and consistent across participants.

The difference is that, unlike in the insula, vmPFC activity after the offer did not predict the answer. And when the authors compared the two regions directly, the effect on choices was significantly different.

So the conclusion is that the effect is specific to one region. Both regions show the same activity pattern, but only the insula's pattern changes decisions in this task. The authors are careful to note that vmPFC results varied a lot between people, so this "no effect" result should be treated with caution.

## Slide 14: Proposed mechanism and supporting evidence  _(~1.25 min)_

Here's the proposed explanation as a chain of four steps.

First, the insula happens to be in a high state just before the offer. Second, because of that, its response to the offer is weaker. It's known that when spontaneous activity is high, the brain's response to a new stimulus tends to be smaller, a bit like a system that is already busy responding less to a new request. Third, a weaker insula response means the unpleasant part of the offer, like losing your keys, carries less weight. Fourth, the person is more likely to accept.

So the state before the offer doesn't vote for an answer directly. It changes how the insula processes what comes next.

Why believe this is specifically about the unpleasant part? Because it fits several independent findings, shown at the bottom. Electrically stimulating the insula changes how much people care about potential losses. People with insula damage struggle to learn from punishment but still learn from rewards. Insula activity tracks bad surprises more than good ones. More insula neurons respond to losses than to gains. And a similar study using a brain scanner, Chew and colleagues in 2019, found that spontaneous activity in a reward-related region also changed people's choices.

## Slide 15: Strengths and weaknesses: how causal is this evidence?  _(~2 min)_

Since this course is about causal approaches, let's ask how strong a causal claim this study can make.

The strip at the top is a simple scale of causal evidence. At the bottom are correlational studies: record brain activity, then sort the trials afterwards and look for a relationship. At the top are interventions like brain stimulation or lesions, where the researcher directly changes the brain and watches what happens to behaviour. This study sits in the middle. It doesn't change the brain, but it controls when the offer arrives relative to the brain's natural state. That's a real step up from sorting afterwards, but it isn't an intervention.

The strengths are on the left. First, the timing is controlled in advance. Trials are assigned to up or down states before the choice happens, so there's no picking of convenient trials after the fact. Second, the comparison is fair. It's the same people and the same task, the conditions alternate, and difficulty and response times were matched, so those can't explain the difference. Third, the recordings come from inside the brain, which gives a precise, local measure of activity. Fourth, there are good controls: trials with epileptic spikes were removed, and the activity flip was absent in the pauses between trials. Fifth, the effect is specific to the insula and not the vmPFC. It also agrees with stimulation and lesion studies, so different methods point to the same conclusion.

The weaknesses are on the right, and the first one is the most important for this course. The brain states are observed, not created. So a hidden third factor, like a momentary change in attention, arousal or mood, could raise insula activity and change the choice at the same time. Without stimulation, we can't rule that out. Second, there's no normal middle condition, so we don't know whether up-states, down-states or both drive the effect. Third, the proposed chain, where the pre-offer state leads to post-offer suppression which leads to the choice, is itself based on correlations within trials. The pre-offer activity didn't predict the choice trial by trial, and the result relied on peak rather than average activity. Fourth, the sample is small, seven insula sessions, with a moderate p-value of 0.04. Finally, the participants are epilepsy patients making imaginary choices, and the vmPFC "no effect" result is hard to interpret, because absence of evidence isn't evidence of absence.

In short, this is stronger than correlational evidence but weaker than an intervention. The natural next step would be to stimulate the insula at the moments the system detects, which would turn this into a true causal test.

## Slide 16: Take-home messages  _(~1 min)_

To wrap up, here are three take-home messages.

First, the method. A closed-loop system can read brain activity live and time each decision to a spontaneous brain state. That turns a correlation question into a controlled comparison: same task, different brain state.

Second, the finding. For hard choices, a spontaneously active insula just before an offer leads to a weaker insula reaction to it, which makes people more willing to accept a deal that mixes something pleasant with something unpleasant.

Third, the bigger picture. The inconsistency in our choices isn't just random noise. Part of it comes from the brain's own moment-to-moment state, and models of decision-making should account for that.

Looking ahead, the authors suggest this could help in conditions where decision-making goes wrong, like addiction, depression or OCD. It could eventually lead to treatments that intervene at exactly the right moment.

## Slide 17: Thank you  _(~0.25 min)_

That concludes my presentation. Thank you for your attention.
