# Artificial Intelligence and Numerical Weather Prediction Models: A Technical Survey

- **Paper:** [Artificial intelligence and numerical weather prediction models: A technical survey](https://doi.org/10.1016/j.nhres.2024.11.004)
- **Authors:** Muhammad Waqas, Usa Wannasingha Humphries, Bunthid Chueasa, and Angkool Wangwongchai
- **Published in:** *Natural Hazards Research*, 5 (2025), 306–320
- **Article type:** Technical survey of peer-reviewed literature from 2000–2024
- **Reading basis:** Full article

> **The main point:** AI can enter a weather-forecasting system at many points. It can help prepare and assimilate observations, tune or emulate parts of a physical model, estimate uncertainty, detect extreme events, and correct forecasts after a numerical model has run. The survey finds post-processing especially promising, while data pre-processing remains difficult. It does not conclude that AI has replaced physics-based NWP across the board.

## What problem is the paper addressing?

A numerical weather prediction system does not simply map the latest observations to tomorrow’s weather. It must first estimate the atmosphere’s present state from incomplete, noisy observations. It then integrates equations for atmospheric motion and thermodynamics. Processes smaller than the model grid—such as parts of turbulence, convection, and cloud microphysics—must be represented through approximations called parameterizations.

The authors organize their review around three questions:

1. What families of weather-forecasting models are used?
2. Where can AI be integrated into an NWP system?
3. How do AI-based approaches compare with conventional physical models, and where are their limits?

This framing is more useful than treating “AI weather forecasting” as one single task. Replacing a costly model component, correcting a model’s output, and extracting features from observations are different jobs with different evidence requirements.


![Original Fig. 2 — Weather prediction models classification and process of weather forecasting](https://ars.els-cdn.com/content/image/1-s2.0-S266659212400091X-gr2.jpg)

*Waqas et al., Fig. 2, journal p. 308. [Original article](https://doi.org/10.1016/j.nhres.2024.11.004) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

The diagram distinguishes model-driven forecasts from data-driven statistical, AI, and hybrid approaches. That distinction sets up the survey’s central question: where can AI improve an NWP system without assuming every AI method replaces the physical model?

## The forecasting chain, in plain language

| Stage | What happens | Why it matters |
|---|---|---|
| Observations | Satellites, radar, stations, and other platforms measure different parts of the atmosphere | No instrument observes the complete atmospheric state everywhere |
| Quality control and pre-processing | Data are checked, aligned, transformed, and sometimes gap-filled | Bad or mismatched inputs can contaminate later stages |
| Data assimilation | Observations are combined with a model background to estimate the current state | Forecast errors grow quickly when the starting state is wrong |
| Model evolution | Physical equations advance the estimated state; unresolved processes are parameterized | This is the core forecast calculation, but it is computationally demanding |
| Post-processing | Model output is bias-corrected, calibrated, downscaled, or converted to probabilities | Raw model output can have systematic local or variable-specific errors |
| Interpretation and decisions | Forecasters and users assess confidence and take action | A useful forecast must communicate when it may fail, not just give a value |

The review’s scope spans most of this chain. Its examples include AI for assimilation and data augmentation; feature extraction and pre-processing; adaptive parameter tuning and optimization; hybrid physical–AI models; uncertainty quantification; extreme-event prediction; and post-processing or interpretation.


![Original Fig. 3 — General working process of a numerical weather prediction model](https://ars.els-cdn.com/content/image/1-s2.0-S266659212400091X-gr3.jpg)

*Waqas et al., Fig. 3, journal p. 309. [Original article](https://doi.org/10.1016/j.nhres.2024.11.004) · [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

In this process, observations help estimate the current atmospheric state; the numerical model advances that state; and forecast products are interpreted and evaluated. This is why AI can be inserted at several stages, from assimilation and parameterization to post-processing.

## What did the authors find?

### 1. AI can support a physical forecast without replacing it

A recurring pattern is a hybrid workflow: the physical model supplies a dynamically informed forecast, while a learned model handles a specific bottleneck. Examples discussed in the survey include machine-learning adjustment of model parameters, learned emulators for expensive components, and corrections to Weather Research and Forecasting (WRF) model outputs.

This distinction matters. A learned correction to WRF output is evidence about that correction task and data setting; it is not evidence that the learned model can replace the whole NWP system.

### 2. Post-processing is a practical and comparatively mature entry point

The survey reviews statistical and machine-learning methods that correct systematic errors, refine spatial detail, or produce calibrated probabilities from existing forecasts. Examples include regression and tree-based methods, neural networks, quantile-based approaches, and ensemble post-processing methods.

The authors highlight post-processing as an area of significant potential because it can build on an existing physical forecast. The benefit still depends on representative training data: a correction learned for one region, season, lead time, or weather regime may not transfer unchanged to another.

### 3. Pre-processing is harder than it sounds

The paper discusses missing values, outliers, feature transformation, normalization, and the preparation of meteorological fields for machine-learning models. It also describes specialized initialization schemes for cloud liquid water. These examples show that pre-processing is not merely a generic “clean the table” step: meteorological variables have physical meaning, spatial structure, and relationships across scales.

A method that removes an unusual observation as an outlier could erase a real extreme event. Likewise, filling gaps or resampling fields can introduce inconsistencies in space or time. The survey therefore treats data quality and physical consistency as central obstacles.

### 4. Uncertainty and extremes need separate evaluation

A good average error score does not establish that a method handles rare, high-impact conditions. The survey covers ensemble and probabilistic approaches, uncertainty estimation, and extreme-event prediction. These methods should be judged on whether their probabilities are calibrated and whether important events are detected—not only on average RMSE or MAE.

The paper is a survey, not a new benchmark experiment. Numerical improvements it reports belong to the individual studies it cites; they are not results from a unified head-to-head test conducted by the survey authors.

## What to take away

- **NWP is a system, not just a neural-network input/output task.** Its initial state, physical integration, unresolved processes, and post-processing all affect the forecast.
- **“AI for weather” describes several distinct interventions.** Always identify which stage a method changes and what its comparison baseline is.
- **Hybrid methods offer a useful way to think about current practice.** AI may improve a component while retaining the physical model’s broader dynamics.
- **Data handling and generalization are scientific issues.** Missingness, observation quality, spatial/temporal alignment, and rare events can change what the model learns.
- **Speed, accuracy, physical consistency, and trust are separate criteria.** A fast forecast is not automatically reliable for every location or hazard.

## Connection to our research

For wind forecasting, the global or regional NWP field can provide the evolving synoptic background, while a local Doppler radar or lidar can provide a much finer view of the wind profile near a site. The paper suggests several *possible roles* for AI in such a system:

1. align and quality-check the model and radar observations;
2. assimilate local measurements or learn a local correction to the background forecast;
3. estimate wind at relevant heights or refine the forecast near a wind farm;
4. quantify uncertainty and flag conditions where the model is poorly supported by data.

These are research hypotheses, not results demonstrated by this survey. Our own evaluation would need to test whether multi-height observations add skill beyond NWP alone, how the gain changes with forecast lead time and weather regime, and whether the learned correction remains reliable during strong shear or rapid ramps.

### One-sentence summary

**Read this paper as a map of where AI can connect to the NWP pipeline—and as a reminder that each connection has its own data, physics, and validation problem.**
