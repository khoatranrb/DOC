# Presentation script: Baratin et al. (2026), *Closed-loop readout of anterior insula high-gamma activity steers value-based decisions*

*Nature Communications*, 2026 · doi:10.1038/s41467-026-75265-5

**16 slides · approx. 21 minutes** (plus Q&A). The same text is in the speaker notes of each slide in the .pptx.

| # | Slide | Time |
|---|---|---|
| 1 | Title | ~0.75 min |
| 2 | Why do we decide differently when facing the same offer? | ~1.5 min |
| 3 | Key concepts | ~1.25 min |
| 4 | The idea: let the brain decide when the offer appears | ~1.25 min |
| 5 | Participants and tasks | ~1.5 min |
| 6 | The closed-loop brain-computer interface | ~1.5 min |
| 7 | Detecting up- and down-states; controlling difficulty | ~1.5 min |
| 8 | Sanity check: choices are value-based | ~1 min |
| 9 | Main result: aIns up-states make people accept more | ~1.5 min |
| 10 | aIns dynamics: high before the offer, suppressed after | ~1.5 min |
| 11 | Which moment predicts the choice? | ~1.25 min |
| 12 | vmPFC: same neural dynamics, no behavioural effect | ~1.25 min |
| 13 | Proposed mechanism and converging evidence | ~1.25 min |
| 14 | Limitations and critical points | ~1.5 min |
| 15 | Take-home messages | ~1 min |
| 16 | Questions for discussion | ~1 min |

---

## Slide 1: Title  _(~0.75 min)_

Good [morning/afternoon], everyone. Today I'm presenting "Closed-loop readout of anterior insula high-gamma activity steers value-based decisions", by Clarissa Baratin, Mathias Pessiglione, Julien Bastin and colleagues from Grenoble and the Paris Brain Institute. It came out in Nature Communications in 2026.

The one-sentence summary: the authors built a brain-computer interface that watches activity inside patients' brains in real time and shows them a decision exactly when a specific brain region happens to be unusually active or unusually quiet. They find that the spontaneous state of the anterior insula at that moment changes what people choose.

So the question running through this talk is: how much of our choice variability comes not from the options in front of us, but from whatever our brain happens to be doing when the options arrive?

## Slide 2: Why do we decide differently when facing the same offer?  _(~1.5 min)_

Let's start with a basic puzzle. If I offer you exactly the same deal twice, you won't always give the same answer. Classical decision models treat that variability as noise around the "true" value of the options.

But there's a growing literature showing that spontaneous fluctuations in brain activity just before a stimulus arrives can bias what we perceive and what we choose. That's been shown for perceptual detection, for free choices, and even for economic decisions.

For value-based decisions, two regions matter most here. The ventromedial prefrontal cortex, vmPFC, and the anterior insula, aIns. Earlier intracranial work from the same group, Cecchi et al. 2022, showed that high pre-stimulus broadband gamma in the vmPFC went with more risk-taking, as if gains were overweighted, especially in positive mood. High activity in the anterior insula went with greater sensitivity to losses, especially in negative mood. fMRI baseline activity in these regions tells a similar story.

The problem (the box on the right) is that all of this is correlational and post-hoc. You record, you sort trials afterwards, and you look for a relationship. You can't choose to present a decision when the brain is in a particular state, so you can't directly test whether that state matters. That's the gap this paper tackles.

## Slide 3: Key concepts  _(~1.25 min)_

A few concepts before the methods.

First, the recordings. These are twelve patients with drug-resistant epilepsy who have depth electrodes implanted for clinical reasons, to localise where their seizures start. This is stereo-EEG, or sEEG. It gives direct recordings from deep structures like the insula with millisecond resolution, which you can't get from the scalp. The brain on the left shows every recording contact used: red for the anterior insula, green for the vmPFC.

Second, the signal. Broadband gamma activity, BGA, is the power between 70 and 150 Hz. It's a well-established proxy for local population spiking, and it correlates with the fMRI BOLD signal, so results can be compared with the imaging literature.

Third, the two regions. The vmPFC is the core valuation hub, encoding subjective value and linked to gains and positive mood. The anterior insula is more tied to aversive processing: losses, punishment prediction errors, negative mood. Keep in mind that in this framework the two regions are often thought of as opponents.

## Slide 4: The idea: let the brain decide when the offer appears  _(~1.25 min)_

So here's the core idea. Instead of presenting trials at fixed times and sorting them afterwards, let the brain decide when each offer appears.

The pipeline runs left to right. They stream the intracranial signal in real time, estimate broadband gamma every 30 milliseconds, and continuously compare it to an adaptive threshold. When the region crosses an "up" threshold, meaning unusually high activity, or a "down" threshold, unusually low activity, the offer is shown immediately. Then the participant decides to accept or reject.

The task and the offers stay the same. The only thing that differs between conditions is the brain state at the moment the offer arrives. That's the neat part of the design.

The hypothesis, from the prior work, was that the two regions would push behaviour in opposite directions. The intuitive prediction is that a vmPFC up-state should favour the pleasant side and so increase acceptance, while an aIns up-state should increase sensitivity to the unpleasant side and so decrease acceptance. Keep that aIns prediction in mind, because the result will be the opposite, and the explanation is one of the most interesting parts of the paper.

## Slide 5: Participants and tasks  _(~1.5 min)_

Now the concrete design. Twelve patients, average age about 34, five women, all monitored at Grenoble University Hospital. Seven sessions were driven by the anterior insula and eight by the vmPFC. Patients with electrodes in both regions did one session for each.

There were two tasks. First, an offline rating task. Participants rated 240 hypothetical scenarios, half pleasant, like "eating a piece of birthday cake", half unpleasant, like "stumbling in public", on a continuous scale of how much they'd like or dislike each one. That gives a personal subjective value for every item.

Second, the real-time accept/reject task. Each offer pairs one pleasant and one unpleasant item: "I would accept losing my house keys in exchange for going on holiday", yes or no. Note the fixation cross has no fixed duration. It stays up until the BCI detects the target brain state. Response time is unlimited.

The key variable is decision value, DV: the pleasant rating minus the unpleasant rating. And importantly, participants were not told that their brain activity controlled when trials appeared.

## Slide 6: The closed-loop brain-computer interface  _(~1.5 min)_

This is Figure 1a, the heart of the method. On the left, the signal comes off the clinical amplifier. The trace at the top shows real-time broadband gamma, in black, with the adaptive "up" threshold in red, the median in grey and the "down" threshold in blue. Each arrow marks a detection, and the trial sequence underneath shows how detections trigger trials: wait, trial 1 on an up-state, wait, trial 2 on a down-state, and so on. The offer then appears on screen and the patient answers with a gamepad.

On the right is the technical pipeline. The Micromed clinical system samples at 512 Hz and streams over TCP/IP. BCI2000 reads the stream and writes it to a FieldTrip buffer, which MATLAB polls. The signal is re-referenced to a bipolar montage between neighbouring contacts, which cleans up distant, volume-conducted activity. Every 16 samples, about 30 ms, they take the last one second of data, apply a Hann window and an FFT, and sum the power from 70 to 150 Hz. That's averaged across bipoles, smoothed over 500 ms, and compared to the threshold. If the threshold is reached, the offer is shown. If nothing happens within 30 seconds, the offer is shown anyway.

## Slide 7: Detecting up- and down-states; controlling difficulty  _(~1.5 min)_

How do they decide what counts as an "up" or "down" state? Intracranial signals are non-stationary: their baseline drifts over a session. So a fixed threshold wouldn't work.

They use a robust moving-median algorithm. Over a sliding 20-second window, they compute the median of the gamma power and its median absolute deviation, or MAD. An up-state is a point more than 3.5 MADs above the median, and a down-state is more than 3.5 MADs below. They compute separate MADs above and below the median, the "double MAD", because the distribution isn't symmetric. Points that cross threshold count only 0.8 in later updates, so one big transient can't hijack the threshold. A nice practical benefit is that there's no calibration period. The thresholds adapt on the fly.

Then the trial design. Each session had 35 up-state and 35 down-state trials, strictly alternating, with a random first trial. Two sessions had 140 trials. To give the brain state the best chance to matter, at least 70% of offers were built to be hard, near each person's indifference point where acceptance is about 50%. A pilot with twelve healthy people showed the pleasant item needs to be rated about 15 points higher than the unpleasant one to reach that point. The intuition: when a choice is easy, the values dominate, and when it's a coin flip, internal state can tip the balance.

## Slide 8: Sanity check: choices are value-based  _(~1 min)_

Before testing the brain-state effect, they check that behaviour looks like normal value-based decision-making. It does.

On the left is Figure 1d: probability of accepting as a function of decision value. The black curve is the group fit and the grey curves are individual participants. A clean sigmoid: the more the pleasant item outweighs the unpleasant one, the more people accept. The slope estimate is 1.15, with a z of almost 17.

Choices were slow, about 8 seconds on average, which fits a deliberative task where you have to imagine two scenarios. And harder choices took longer, as you'd expect.

The most important point for what follows is on the right. Up-state and down-state trials didn't differ in decision value or in choice time. So any behavioural difference between states can't be explained by one condition simply having easier or harder offers.

## Slide 9: Main result: aIns up-states make people accept more  _(~1.5 min)_

Here is the main result. In sessions driven by the anterior insula, offers presented during up-states were accepted more often than offers presented during down-states.

On the left, Figure 2b: acceptance rate for up versus down trials. Each line is a participant, and most of them slope downward from up to down. In a mixed-effects logistic regression that controls for decision value and inter-trial interval, the up-state effect is beta 0.44, p = 0.04.

One obvious worry with epilepsy patients is that pathological activity, like interictal spikes or high-frequency oscillations, could be triggering the "up-states". So they detected those events automatically, checked them by eye, and removed the affected trials. The effect held, and actually got a bit stronger: beta 0.47, p = 0.014.

Now remember the prediction. Given the insula's link to losses, you'd expect high insula activity to make people more averse to the unpleasant component and to accept less. They found the opposite. The next two slides explain why.

## Slide 10: aIns dynamics: high before the offer, suppressed after  _(~1.5 min)_

The authors then looked at what happens in the insula after the offer appears, even though the trials were only classified by activity at offer onset.

Left panel, Figure 2c: the time-frequency contrast, up minus down. Warm colours before time zero are expected, since that's how the trials were selected. After onset, a cooler, bluish pattern appears in the high frequencies.

The middle panel, 2d, makes it clearer. The red line is up-state trials and the blue line is down-state trials. Red peaks at offer onset by construction, then drops below baseline and stays suppressed through the shaded 2.5 to 4.5 second window. Blue does the reverse: it rises after the offer. So there's a crossover, where high before means low after, and low before means high after.

The right panel, 2e, quantifies it per participant: the up minus down difference is positive before the offer and negative after it, in every participant. Statistically, the state-by-time-window interaction is huge: t about 9.5, p around 10 to the minus 20.

A key control: this reversal doesn't happen during inter-trial intervals. When there's no offer, up-state events stay higher than down-state events in both windows. So the reversal isn't just regression to the mean. It depends on engaging with the task. It's consistent with known anti-correlations between spontaneous and stimulus-evoked activity.

## Slide 11: Which moment predicts the choice?  _(~1.25 min)_

So we have two candidate signals: activity before the offer and activity after it. Which one actually relates to the choice, trial by trial?

They ran logistic mixed models with choice as the outcome and gamma peak amplitude in one of three windows as the predictor, controlling for decision value.

The pre-offer peak, which is the thing the BCI used, did not predict choice on a trial-by-trial basis: p = 0.20. Activity in the last second before the response didn't either: p = 0.11. But the post-offer peak did: beta negative, p = 0.03. The lower the insula activity after the offer, the more likely people were to accept.

There's no interaction with decision value, so the effect is similar across the range of difficulties tested. In an exploratory analysis, the theta band, 4 to 8 Hz, showed a similar pattern.

Putting it together: high pre-offer activity leads to post-offer suppression, and that suppression is what biases people towards accepting the unpleasant item in exchange for the pleasant one. The pre-stimulus state seems to act indirectly, through how the region responds to the offer.

## Slide 12: vmPFC: same neural dynamics, no behavioural effect  _(~1.25 min)_

Now the second region, the vmPFC. In sessions driven by vmPFC activity, up versus down states did not change choices: beta essentially zero, p = 0.89. On the left, Figure 2f, the individual lines go in both directions. Some participants accepted more in up-states, others less.

You might think the BCI just failed to capture meaningful vmPFC states. But it didn't. The middle panel, 2h, shows the same pre-to-post reversal we saw in the insula: up-state trials drop well below baseline after the offer, and down-state trials go up. The interaction is just as strong, p around 10 to the minus 18, and consistent across participants, as panel 2i on the right shows.

But unlike the insula, post-offer vmPFC activity did not predict choice. And when they directly compared the two regions, the up-down effect on acceptance was significantly different between aIns and vmPFC.

So the message is anatomical specificity. Both regions show structured, state-dependent dynamics, but only the insula's fluctuations translate into a behavioural bias in this task. The authors are careful here, and so should we be: the vmPFC effect was very variable across people, so this null result shouldn't be over-interpreted as a true functional dissociation.

## Slide 13: Proposed mechanism and converging evidence  _(~1.25 min)_

Here's the proposed mechanism as a causal chain. Spontaneously high insula activity just before the offer leads to a suppressed insula response to that offer. That fits a known principle: spontaneous and evoked activity tend to be anti-correlated. Less insula response means less weight on the aversive part of the offer, like losing your keys. And less weight on the aversive part means you're more likely to accept.

So the pre-stimulus state doesn't directly "vote" for an option. It changes how the region processes what comes next.

Why believe this is about aversive weighting specifically? Because it fits several independent lines of evidence, shown at the bottom. Electrical stimulation of the insula changes how much potential losses matter in risky choice. Insula lesions impair learning from punishment but spare reward learning. Insular gamma tracks punishment prediction errors more than reward ones. Pre-stimulus insula gamma tracks negative mood but not positive mood. And more single insula neurons encode losses than gains. There's also a nice parallel with a real-time fMRI study of the dopaminergic midbrain, Chew et al. 2019, where endogenous fluctuations also drove choice variability.

## Slide 14: Limitations and critical points  _(~1.5 min)_

Every study has limits, and I've split them into two groups.

On the left are the limitations the authors acknowledge. There was no intermediate or control condition, only up versus down, so we can't tell whether up-states increase acceptance, down-states decrease it, or both. Spatial sampling is limited to a few contacts per patient. Theta behaved like gamma, which is a bit unexpected since theta is usually anti-correlated with gamma and BOLD, so the effect may reflect a broader modulation across frequencies. The authors themselves say the causal interpretation should be cautious. And the vmPFC null is surprising given the literature.

On the right are points I think are worth discussing. First, sample size. There are seven insula sessions, and the main effect is p = 0.04, which is modest and needs replication. Second, "steers" in the title is strong. The closed-loop design samples naturally occurring states. It doesn't create them, since there's no stimulation. That's better than post-hoc sorting because timing is controlled, but it's still not an intervention. Third, the trial-by-trial effect depends on a peak-based measure. The authors report that mean gamma in the same windows didn't predict choice. Fourth, the choices are hypothetical, with no real outcomes. And finally, these are epilepsy patients, so generalisation to healthy brains is an assumption, although the pathological-activity control helps.

## Slide 15: Take-home messages  _(~1 min)_

To wrap up, three take-home messages.

One, methodological. A closed-loop intracranial BCI can present decisions at chosen moments of spontaneous brain activity, with adaptive thresholds and no calibration. That turns a correlational question into a controlled comparison where the task stays constant and only the brain state changes.

Two, the finding. For hard choices, spontaneous up-states in the anterior insula make people more likely to accept offers that mix pleasant and unpleasant outcomes, apparently because they're followed by a suppressed insula response, which reduces the weight of the aversive part.

Three, the broader point. Choice variability isn't just noise. Part of it comes from intrinsic brain states, and neuro-computational models of decision-making will need to take that into account.

Looking ahead, the authors suggest this could matter in disorders where decision-making goes wrong, such as OCD, addiction or depression, and could eventually inform closed-loop neuromodulation that intervenes at the right moment.

## Slide 16: Questions for discussion  _(~1 min)_

Thank you for your attention. I'll leave a few questions to start the discussion.

First: is sampling spontaneous states enough to claim that activity "steers" decisions, or do we need stimulation, for example triggering insula stimulation at detected states?

Second: why would the vmPFC show the same neural reversal but no behavioural effect? Is it the task, which uses hypothetical scenarios rather than money? The sample size? Or the way value is represented there?

Third: if the pre-offer state acts through the post-offer response, can we model it formally, for example as a shift in the weight on losses, or in the starting point of a drift-diffusion process?

And finally, could state-aware timing be used practically, for example to reduce maladaptive choices in addiction or depression?

I'm happy to take any questions.
