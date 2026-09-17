# RLVR: actual before/after results

Every answer below is a saved model generation. Before: the original checkpoint. After: a fresh LoRA trained only with programmatic rewards on 256 synthetic training prompts; no workshop SFT, supplied answer targets, teacher API, or best-of-N selection. Both receive identical task instructions.

Strict success measures the task rules. For microfiction it does **not** measure storytelling quality. Greedy first attempts are the main comparison; fixed-seed sampling is shown separately. Small single-seed experiments demonstrate behavior, not a general model ranking.

| Task | Model | Dev before → after | Test before → after | Training | Estimated compute |
|---|---|---:|---:|---:|---:|
| six_words | Qwen/Qwen3-0.6B | 0/24 → 0/24 | 0/32 → 0/32 | 230.8 s | $0.0754 |
| countdown | Qwen/Qwen3-0.6B | 0/24 → 3/24 | 0/32 → 2/32 | 190.1 s | $0.0685 |
| maze | Qwen/Qwen3-0.6B | 0/24 → 0/24 | 0/32 → 0/32 | 91.2 s | $0.0342 |

Compute estimates cover completed workers including evaluation and reload, excluding startup/storage. Screening and any follow-up runs are additional; see LAB_NOTEBOOK.md.

## six_words: rlvr-train-six_words-1788799386079459022

Model: **Qwen/Qwen3-0.6B**, revision `c1899de289a04d12100db370d81485cdf75e47ca`. After: RLVR on this task only, 160 batches / 69 updates, rank-16 LoRA, LR 0.0002, beta 0. Selected batch 160; checkpoint selection disabled (final batch). Data SHA-256 `750abfd1a44f8d94e03f7f686577aa146f0ae4c486279c6f0bb6966ba9b16570`. Fresh-base adapter reload matches: True.

Sampling uses temperature 1, top-k 0, top-p 1; evaluation seed 2026. Greedy evaluation uses batches of eight. No decoding repair or retry.

### dev

#### six_words-dev-000 / 1

Write a tiny story in exactly SIX English words. Include the exact words "moon" and "sailor". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.400:

```text
moon sailor sails
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Moon who is a sailor.
```

#### six_words-dev-001 / 2

Write a tiny story in exactly SIX English words. Include the exact words "clown" and "ocean". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.200:

```text
clown oceancan be a magical creature that dances on the ocean's surface.
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Clown who is an ocean.
```

#### six_words-dev-002 / 3

Write a tiny story in exactly SIX English words. Include the exact words "teacher" and "thunder". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
teacher thunder
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Thunder who is a teacher.
```

#### six_words-dev-003 / 4

Write a tiny story in exactly SIX English words. Include the exact words "queen" and "sailor". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.467:

```text
queen sailor sails the sea
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Queen who is a sailor.
```

#### six_words-dev-004 / 5

Write a tiny story in exactly SIX English words. Include the exact words "key" and "wolf". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
key wolf
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Wolf who is the key.
```

#### six_words-dev-005 / 6

Write a tiny story in exactly SIX English words. Include the exact words "candle" and "dragon". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
candle dragon
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Candle who is a dragon.
```

#### six_words-dev-006 / 7

Write a tiny story in exactly SIX English words. Include the exact words "chef" and "forest". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
chef forest
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Chef who is a forest.
```

#### six_words-dev-007 / 8

Write a tiny story in exactly SIX English words. Include the exact words "dragon" and "key". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
dragon key
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Dragon who is the key.
```

#### six_words-dev-008 / 9

Write a tiny story in exactly SIX English words. Include the exact words "candle" and "letter". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
candle letter
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Candle who is a letter.
```

#### six_words-dev-009 / 10

Write a tiny story in exactly SIX English words. Include the exact words "coffee" and "wolf". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
coffee wolf
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Coffee who is a wolf.
```

#### six_words-dev-010 / 11

Write a tiny story in exactly SIX English words. Include the exact words "sailor" and "violin". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.400:

```text
sailor plays violin
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Sailor who is a violin.
```

#### six_words-dev-011 / 12

Write a tiny story in exactly SIX English words. Include the exact words "raven" and "spaceship". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.267:

```text
raven spaceships
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Raven who is a spaceship.
```

#### six_words-dev-012 / 13

Write a tiny story in exactly SIX English words. Include the exact words "mouse" and "rain". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
mouse rain
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Mouse who is a rain.
```

#### six_words-dev-013 / 14

Write a tiny story in exactly SIX English words. Include the exact words "doctor" and "forest". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.433:

```text
doctor in the forest
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Forest who is a doctor.
```

#### six_words-dev-014 / 15

Write a tiny story in exactly SIX English words. Include the exact words "owl" and "wizard". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
owl wizard
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Owl who is a wizard.
```

#### six_words-dev-015 / 16

Write a tiny story in exactly SIX English words. Include the exact words "fox" and "moon". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.400:

```text
fox and moon.
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Fox who is a moon.
```

#### six_words-dev-016 / 17

Write a tiny story in exactly SIX English words. Include the exact words "alien" and "princess". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.300:

```text
alien princess princess
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Alien who is a princess.
```

#### six_words-dev-017 / 18

Write a tiny story in exactly SIX English words. Include the exact words "rabbit" and "sailor". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.400:

```text
rabbit sailor sails
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Rabbit who is a sailor.
```

#### six_words-dev-018 / 19

Write a tiny story in exactly SIX English words. Include the exact words "dog" and "queen". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
dog queen
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Dog who is a queen.
```

#### six_words-dev-019 / 20

Write a tiny story in exactly SIX English words. Include the exact words "farmer" and "sunrise". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.400:

```text
farmer at sunrise
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Farmer who is a sunrise.
```

#### six_words-dev-020 / 21

Write a tiny story in exactly SIX English words. Include the exact words "moon" and "princess". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.333:

```text
moon princess princess moon
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Moon who is a princess.
```

#### six_words-dev-021 / 22

Write a tiny story in exactly SIX English words. Include the exact words "mirror" and "wizard". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
mirror wizard
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Mirror who is a wizard.
```

#### six_words-dev-022 / 23

Write a tiny story in exactly SIX English words. Include the exact words "ocean" and "wolf". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
ocean wolf
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Ocean who is a wolf.
```

#### six_words-dev-023 / 24

Write a tiny story in exactly SIX English words. Include the exact words "doctor" and "pilot". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
doctor pilot
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Doctor who is a pilot.
```

### test

#### six_words-test-000 / 1

Write a tiny story in exactly SIX English words. Include the exact words "dog" and "painter". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.333:

```text
dog painter paints dog
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Dog who is a painter.
```

#### six_words-test-001 / 2

Write a tiny story in exactly SIX English words. Include the exact words "island" and "pilot". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.333:

```text
island pilot is island
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Island who is a pilot.
```

#### six_words-test-002 / 3

Write a tiny story in exactly SIX English words. Include the exact words "library" and "sunrise". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
library sunrise
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Library who is a sunrise.
```

#### six_words-test-003 / 4

Write a tiny story in exactly SIX English words. Include the exact words "mouse" and "vampire". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
mouse vampire
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Mouse who is a vampire.
```

#### six_words-test-004 / 5

Write a tiny story in exactly SIX English words. Include the exact words "dragon" and "raven". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
dragon raven
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Dragon who is a raven.
```

#### six_words-test-005 / 6

Write a tiny story in exactly SIX English words. Include the exact words "rabbit" and "spaceship". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
rabbit spaceship
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Rabbit who is a spaceship.
```

#### six_words-test-006 / 7

Write a tiny story in exactly SIX English words. Include the exact words "thunder" and "tiger". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.267:

```text
thunder tigers
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Thunder who is a tiger.
```

#### six_words-test-007 / 8

Write a tiny story in exactly SIX English words. Include the exact words "mouse" and "wolf". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
mouse wolf
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Mouse who is a wolf.
```

#### six_words-test-008 / 9

Write a tiny story in exactly SIX English words. Include the exact words "castle" and "wedding". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
castle wedding
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Castle who is a wedding.
```

#### six_words-test-009 / 10

Write a tiny story in exactly SIX English words. Include the exact words "suitcase" and "tiger". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
suitcase tiger
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.367:

```text
 Suit who is a tiger.
```

#### six_words-test-010 / 11

Write a tiny story in exactly SIX English words. Include the exact words "astronaut" and "birthday". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
astronaut birthday
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Astronaut who is a birthday.
```

#### six_words-test-011 / 12

Write a tiny story in exactly SIX English words. Include the exact words "coffee" and "key". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
coffee key
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Coffee who is the key.
```

#### six_words-test-012 / 13

Write a tiny story in exactly SIX English words. Include the exact words "candle" and "robot". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
candle robot
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Candle who is a robot.
```

#### six_words-test-013 / 14

Write a tiny story in exactly SIX English words. Include the exact words "funeral" and "umbrella". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.333:

```text
funeral umbrella funeral umbrella
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Funeral who is an umbrella.
```

#### six_words-test-014 / 15

Write a tiny story in exactly SIX English words. Include the exact words "chef" and "robot". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
chef robot
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Chef who is a robot.
```

#### six_words-test-015 / 16

Write a tiny story in exactly SIX English words. Include the exact words "clown" and "forest". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.433:

```text
clown in the forest
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Clown who is a forest.
```

#### six_words-test-016 / 17

Write a tiny story in exactly SIX English words. Include the exact words "portrait" and "violinist". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.433:

```text
portrait of a violinist.
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Portrait who is a violinist.
```

#### six_words-test-017 / 18

Write a tiny story in exactly SIX English words. Include the exact words "penguin" and "portrait". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
penguin portrait
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Penguin who is a portrait.
```

#### six_words-test-018 / 19

Write a tiny story in exactly SIX English words. Include the exact words "circus" and "glacier". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.300:

```text
glacier circus circus
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Circus who is a glacier.
```

#### six_words-test-019 / 20

Write a tiny story in exactly SIX English words. Include the exact words "circus" and "dinosaur". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.200:

```text
circus dino circus
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Circus who is a dinosaur.
```

#### six_words-test-020 / 21

Write a tiny story in exactly SIX English words. Include the exact words "desert" and "telescope". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
desert telescope
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Desert who is a telescope.
```

#### six_words-test-021 / 22

Write a tiny story in exactly SIX English words. Include the exact words "telescope" and "volcano". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
telescope volcano
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Telescope who is a volcano.
```

#### six_words-test-022 / 23

Write a tiny story in exactly SIX English words. Include the exact words "balloon" and "telescope". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
balloon telescope
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Balloon who is a telescope.
```

#### six_words-test-023 / 24

Write a tiny story in exactly SIX English words. Include the exact words "mermaid" and "notebook". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.400:

```text
mermaid notebook note
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Mermaid who is a notebook.
```

#### six_words-test-024 / 25

Write a tiny story in exactly SIX English words. Include the exact words "mushroom" and "violinist". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
violinist mushrooms in the forest
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Mushroom who is a violinist.
```

#### six_words-test-025 / 26

Write a tiny story in exactly SIX English words. Include the exact words "dinosaur" and "mushroom". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
dinosaur mushroom
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.367:

```text
inosaur who is a mushroom.
```

#### six_words-test-026 / 27

Write a tiny story in exactly SIX English words. Include the exact words "balloon" and "circus". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.433:

```text
balloon in the circus
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Balloon who is a circus.
```

#### six_words-test-027 / 28

Write a tiny story in exactly SIX English words. Include the exact words "balloon" and "mermaid". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
balloon mermaid
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Balloon who is a mermaid.
```

#### six_words-test-028 / 29

Write a tiny story in exactly SIX English words. Include the exact words "submarine" and "volcano". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
submarine volcano
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Submarine who is a volcano.
```

#### six_words-test-029 / 30

Write a tiny story in exactly SIX English words. Include the exact words "glacier" and "mermaid". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
glacier mermaid
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Glacier who is a mermaid.
```

#### six_words-test-030 / 31

Write a tiny story in exactly SIX English words. Include the exact words "comet" and "dinosaur". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
comet dinosaur
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Comet who is a dinosaur.
```

#### six_words-test-031 / 32

Write a tiny story in exactly SIX English words. Include the exact words "penguin" and "volcano". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
penguin volcano
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Penguin who is a volcano.
```

### sampled_dev

#### six_words-dev-000 / 1

Write a tiny story in exactly SIX English words. Include the exact words "moon" and "sailor". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
moon in the sailor's path.
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Moon who is a sailor.
```

#### six_words-dev-000 / 2

Write a tiny story in exactly SIX English words. Include the exact words "moon" and "sailor". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.400:

```text
moon sailor sails
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Moon who is a sailor.
```

#### six_words-dev-001 / 3

Write a tiny story in exactly SIX English words. Include the exact words "clown" and "ocean". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
clown ocean
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Clown who is an ocean.
```

#### six_words-dev-001 / 4

Write a tiny story in exactly SIX English words. Include the exact words "clown" and "ocean". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.433:

```text
clown at the ocean.
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Clown who is the ocean.
```

#### six_words-dev-002 / 5

Write a tiny story in exactly SIX English words. Include the exact words "teacher" and "thunder". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
teacher thunder
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Thunder who is a teacher.
```

#### six_words-dev-002 / 6

Write a tiny story in exactly SIX English words. Include the exact words "teacher" and "thunder". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
teacher thunder
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Thunder who is a teacher.
```

#### six_words-dev-003 / 7

Write a tiny story in exactly SIX English words. Include the exact words "queen" and "sailor". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.400:

```text
queen sailor sailed.
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Queen who is a sailor.
```

#### six_words-dev-003 / 8

Write a tiny story in exactly SIX English words. Include the exact words "queen" and "sailor". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.433:

```text
queen savior sailor galaxy
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Queen who is a sailor.
```

#### six_words-dev-004 / 9

Write a tiny story in exactly SIX English words. Include the exact words "key" and "wolf". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
key wolf
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Wolf who is the key.
```

#### six_words-dev-004 / 10

Write a tiny story in exactly SIX English words. Include the exact words "key" and "wolf". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
key wolf
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Wolf who is the key.
```

#### six_words-dev-005 / 11

Write a tiny story in exactly SIX English words. Include the exact words "candle" and "dragon". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
candle dragon
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Candle who is a dragon.
```

#### six_words-dev-005 / 12

Write a tiny story in exactly SIX English words. Include the exact words "candle" and "dragon". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.400:

```text
candle dragon flame
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Candle who is a dragon.
```

#### six_words-dev-006 / 13

Write a tiny story in exactly SIX English words. Include the exact words "chef" and "forest". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
chef forest
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Chef who is the forest.
```

#### six_words-dev-006 / 14

Write a tiny story in exactly SIX English words. Include the exact words "chef" and "forest". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
chef forest
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Chef who is the forest.
```

#### six_words-dev-007 / 15

Write a tiny story in exactly SIX English words. Include the exact words "dragon" and "key". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
dragon key
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Dragon who is the key.
```

#### six_words-dev-007 / 16

Write a tiny story in exactly SIX English words. Include the exact words "dragon" and "key". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
dragon key
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Dragon who is the key.
```

#### six_words-dev-008 / 17

Write a tiny story in exactly SIX English words. Include the exact words "candle" and "letter". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.400:

```text
lighted candle letter
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Candle who is a letter.
```

#### six_words-dev-008 / 18

Write a tiny story in exactly SIX English words. Include the exact words "candle" and "letter". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
candle letter
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Candle who is the letter.
```

#### six_words-dev-009 / 19

Write a tiny story in exactly SIX English words. Include the exact words "coffee" and "wolf". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
coffee wolf
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Coffee who is a wolf.
```

#### six_words-dev-009 / 20

Write a tiny story in exactly SIX English words. Include the exact words "coffee" and "wolf". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.367:

```text
coffee! wolf!
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Coffee who is a wolf.
```

#### six_words-dev-010 / 21

Write a tiny story in exactly SIX English words. Include the exact words "sailor" and "violin". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.433:

```text
sailor violin heed easily
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.367:

```text
 Sail who is a violin.
```

#### six_words-dev-010 / 22

Write a tiny story in exactly SIX English words. Include the exact words "sailor" and "violin". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.433:

```text
sailor plays the violin
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Sailor who is a violin.
```

#### six_words-dev-011 / 23

Write a tiny story in exactly SIX English words. Include the exact words "raven" and "spaceship". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.233:

```text
ravend as spacef seat
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Raven who is a spaceship.
```

#### six_words-dev-011 / 24

Write a tiny story in exactly SIX English words. Include the exact words "raven" and "spaceship". Use each word only once. Return only the story, on one line, with no title or explanation. Words are sequences of letters; punctuation does not count.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.433:

```text
raven spaceship from space
```

After — Qwen/Qwen3-0.6B + six_words RLVR; success=False; reward=0.467:

```text
 Raven who is a spaceship.
```

## countdown: rlvr-train-countdown-1788799671247002331

Model: **Qwen/Qwen3-0.6B**, revision `c1899de289a04d12100db370d81485cdf75e47ca`. After: RLVR on this task only, 160 batches / 14 updates, rank-16 LoRA, LR 0.0002, beta 0. Selected batch 160; checkpoint selection disabled (final batch). Data SHA-256 `7c4f124395a8a3f5e3a4bf99d8e5be077a1fe47c1cad2bc0f40b8543e2406565`. Fresh-base adapter reload matches: True.

Sampling uses temperature 1, top-k 0, top-p 1; evaluation seed 2026. Greedy evaluation uses batches of eight. No decoding repair or retry.

### dev

#### countdown-dev-000 / 1

Countdown puzzle: use the numbers [2, 11, 2] exactly once each to make 24. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
2 + 11 + 2 = 24
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.511:

```text
2 + 11 - 2
```

#### countdown-dev-001 / 2

Countdown puzzle: use the numbers [13, 2, 2] exactly once each to make 13. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
13 = 2 * 2 + 13
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=True; reward=1.000:

```text
13 + 2 - 2
```

#### countdown-dev-002 / 3

Countdown puzzle: use the numbers [10, 4, 12] exactly once each to make 18. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
10 + 4 + 12 = 18
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.509:

```text
10 + 4 - 12
```

#### countdown-dev-003 / 4

Countdown puzzle: use the numbers [9, 9, 12] exactly once each to make 117. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
9 + 9 + 12 = 117
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.501:

```text
9 + 9 - 12
```

#### countdown-dev-004 / 5

Countdown puzzle: use the numbers [11, 7, 15] exactly once each to make 19. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
11 + 7 + 15 = 33  
11 + 7 + 15 = 33  

**Answer:** 11 + 7 + 15 = 33
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.509:

```text
11 + 7 - 15
```

#### countdown-dev-005 / 6

Countdown puzzle: use the numbers [5, 4, 10] exactly once each to make 54. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
5 + 4 + 10 = 54
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
5 + 4 - 10
```

#### countdown-dev-006 / 7

Countdown puzzle: use the numbers [11, 10, 12] exactly once each to make 11. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
11 + 10 - 12 = 11
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.550:

```text
11 + 10 - 12
```

#### countdown-dev-007 / 8

Countdown puzzle: use the numbers [4, 12, 5] exactly once each to make 68. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
4 * 12 + 5 = 68
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
4 + 12 - 5
```

#### countdown-dev-008 / 9

Countdown puzzle: use the numbers [8, 2, 4] exactly once each to make 16. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 2 + 4 = 14  
8 + 2 * 4 = 16
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.514:

```text
8 + 2 - 4
```

#### countdown-dev-009 / 10

Countdown puzzle: use the numbers [6, 7, 12] exactly once each to make 54. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
6 * 7 + 12 = 54
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
6 + 7 - 12
```

#### countdown-dev-010 / 11

Countdown puzzle: use the numbers [6, 2, 15] exactly once each to make 36. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
6 + 15 + 2 = 23  
(6 + 15) + 2 = 23  
6 * 2 + 15 = 36
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
6 + 2 - 15
```

#### countdown-dev-011 / 12

Countdown puzzle: use the numbers [8, 14, 5] exactly once each to make 117. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 14 + 5 = 27  
But this is not 117. Let's try again.

8 * 14 + 5 = 112  
Still not 117.
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.501:

```text
8 + 14 - 5
```

#### countdown-dev-012 / 13

Countdown puzzle: use the numbers [3, 2, 3] exactly once each to make 9. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
3 + 2 + 3 = 9
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.519:

```text
3 + 2 - 3
```

#### countdown-dev-013 / 14

Countdown puzzle: use the numbers [6, 12, 15] exactly once each to make 21. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
6 + 12 + 15 = 33
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.508:

```text
6 + 12 - 15
```

#### countdown-dev-014 / 15

Countdown puzzle: use the numbers [6, 11, 13] exactly once each to make 89. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
6 + 11 + 13 = 89
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.502:

```text
6 + 11 - 13
```

#### countdown-dev-015 / 16

Countdown puzzle: use the numbers [3, 13, 11] exactly once each to make 21. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
3 + 11 + 13 = 27  
(3 + 11) + 13 = 27  
3 + 13 + 11 = 27  

**Answer:** 
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.509:

```text
3 + 13 - 11
```

#### countdown-dev-016 / 17

Countdown puzzle: use the numbers [2, 10, 9] exactly once each to make 92. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.200:

```text
92
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.502:

```text
2 + 10 - 9
```

#### countdown-dev-017 / 18

Countdown puzzle: use the numbers [11, 13, 6] exactly once each to make 18. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
11 + 6 + 13 = 18
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=True; reward=1.000:

```text
11 + 13 - 6
```

#### countdown-dev-018 / 19

Countdown puzzle: use the numbers [7, 10, 2] exactly once each to make 24. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
7 + 10 + 2 = 19  
7 + 10 - 2 = 17  
7 * 10 - 2 = 68  
7 * 2 + 10 =
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.515:

```text
7 + 10 - 2
```

#### countdown-dev-019 / 20

Countdown puzzle: use the numbers [2, 7, 5] exactly once each to make 10. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
2 + 7 - 5 = 4
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.521:

```text
2 + 7 - 5
```

#### countdown-dev-020 / 21

Countdown puzzle: use the numbers [15, 8, 15] exactly once each to make 8. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
15 + 8 = 23  
But that's not 8. Let's try again.  

15 - 8 = 7  
Still not 8.  

15 / 8 = 1.8
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=True; reward=1.000:

```text
15 + 8 - 15
```

#### countdown-dev-021 / 22

Countdown puzzle: use the numbers [2, 15, 11] exactly once each to make 37. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
2 + 15 + 11 = 37
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.505:

```text
2 + 15 - 11
```

#### countdown-dev-022 / 23

Countdown puzzle: use the numbers [13, 3, 10] exactly once each to make 43. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
3 + 10 + 13 = 43
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.504:

```text
13 + 3 - 10
```

#### countdown-dev-023 / 24

Countdown puzzle: use the numbers [4, 4, 14] exactly once each to make 30. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
4 + 14 = 18  
18 + 4 = 22  
22 + 4 = 26  
26 + 4 = 30  

**Answer:** 4 + 1
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.504:

```text
4 + 4 - 14
```

### test

#### countdown-test-000 / 1

Countdown puzzle: use the numbers [8, 10, 2] exactly once each to make 4. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 10 - 2 = 16
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.512:

```text
8 + 10 - 2
```

#### countdown-test-001 / 2

Countdown puzzle: use the numbers [7, 6, 14] exactly once each to make 91. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
7 + 6 + 14 = 27  
**7 + 6 + 14 = 27**
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.502:

```text
7 + 6 - 14
```

#### countdown-test-002 / 3

Countdown puzzle: use the numbers [8, 14, 7] exactly once each to make 119. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 14 + 7 = 29  
But this doesn't equal 119. Let's try again.

8 * 14 = 112  
112 + 7 = 1
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.501:

```text
8 + 14 - 7
```

#### countdown-test-003 / 4

Countdown puzzle: use the numbers [10, 5, 6] exactly once each to make 40. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
10 + 5 + 6 + 10 = 21  
Wait, that's not correct. Let me try again.

Let me try:

10 + 5 + 6 = 21  
But we
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.505:

```text
10 + 5 - 6
```

#### countdown-test-004 / 5

Countdown puzzle: use the numbers [3, 10, 5] exactly once each to make 53. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
3 + 10 + 5 = 18  
3 + 10 + 5 = 18  
3 + 10 + 5 = 18  

(3 + 10) * 
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
3 + 10 - 5
```

#### countdown-test-005 / 6

Countdown puzzle: use the numbers [10, 5, 15] exactly once each to make 85. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
10 + 5 + 15 = 30  
10 + 5 * 15 = 100  
10 + 5 + 15 = 30  
10 * 5
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.502:

```text
10 + 5 - 15
```

#### countdown-test-006 / 7

Countdown puzzle: use the numbers [8, 13, 6] exactly once each to make 86. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 13 + 6 = 27  
8 + 13 * 6 = 86
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.502:

```text
8 + 13 - 6
```

#### countdown-test-007 / 8

Countdown puzzle: use the numbers [3, 6, 4] exactly once each to make 22. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
3 + 6 + 4 = 13  
3 + 6 + 4 = 13  
3 + 6 + 4 = 13  

(3 + 6) + 4 = 1
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.508:

```text
3 + 6 - 4
```

#### countdown-test-008 / 9

Countdown puzzle: use the numbers [8, 11, 6] exactly once each to make 114. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 11 + 6 = 25  
**8 + 11 + 6 = 25**
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.501:

```text
8 + 11 - 6
```

#### countdown-test-009 / 10

Countdown puzzle: use the numbers [14, 10, 13] exactly once each to make 144. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
14 * 10 + 13 = 144
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.501:

```text
14 + 10 - 13
```

#### countdown-test-010 / 11

Countdown puzzle: use the numbers [15, 7, 3] exactly once each to make 36. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.200:

```text
36
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.508:

```text
15 + 7 - 3
```

#### countdown-test-011 / 12

Countdown puzzle: use the numbers [4, 12, 14] exactly once each to make 6. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
4 + 12 = 16  
16 - 14 = 2
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.530:

```text
4 + 12 - 14
```

#### countdown-test-012 / 13

Countdown puzzle: use the numbers [7, 10, 8] exactly once each to make 5. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
7 + 10 - 8 = 9
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.530:

```text
7 + 10 - 8
```

#### countdown-test-013 / 14

Countdown puzzle: use the numbers [5, 9, 11] exactly once each to make 64. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
5 + 9 + 11 = 25  
5 + 9 + 11 = 25  
5 + 9 + 11 = 25  

(5 + 9) * 1
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.502:

```text
5 + 9 - 11
```

#### countdown-test-014 / 15

Countdown puzzle: use the numbers [8, 6, 15] exactly once each to make 17. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 6 + 15 = 29  
(8 + 6) + 15 = 29
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.508:

```text
8 + 6 - 15
```

#### countdown-test-015 / 16

Countdown puzzle: use the numbers [15, 6, 14] exactly once each to make 99. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
15 + 6 + 14 = 35  
**15 + 6 + 14 = 35**
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.502:

```text
15 + 6 - 14
```

#### countdown-test-016 / 17

Countdown puzzle: use the numbers [4, 6, 6] exactly once each to make 30. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
4 + 6 + 6 = 16  
4 + 6 * 6 = 40  
4 * 6 + 6 = 30  

Let me know if you'd like a different solution!
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.506:

```text
4 + 6 - 6
```

#### countdown-test-017 / 18

Countdown puzzle: use the numbers [4, 2, 11] exactly once each to make 52. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
4 + 11 + 2 = 17  
4 * 11 + 2 = 46  
4 * 2 + 11 = 28  
4 * 11 + 2 =
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
4 + 2 - 11
```

#### countdown-test-018 / 19

Countdown puzzle: use the numbers [10, 9, 4] exactly once each to make 3. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
10 + 9 - 4 = 5
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.512:

```text
10 + 9 - 4
```

#### countdown-test-019 / 20

Countdown puzzle: use the numbers [8, 5, 6] exactly once each to make 3. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 5 = 13  
5 + 6 = 11  
8 + 6 = 14  
5 + 6 = 11  
8 * 5 = 40  
5 * 
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.530:

```text
8 + 5 - 6
```

#### countdown-test-020 / 21

Countdown puzzle: use the numbers [12, 13, 3] exactly once each to make 51. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
12 + 13 + 3 = 28  
(12 + 13) + 3 = 28  
12 * 13 = 156  
156 / 3
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.505:

```text
12 + 13 - 3
```

#### countdown-test-021 / 22

Countdown puzzle: use the numbers [13, 14, 3] exactly once each to make 53. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
13 + 14 + 3 = 53
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.505:

```text
13 + 14 - 3
```

#### countdown-test-022 / 23

Countdown puzzle: use the numbers [5, 10, 9] exactly once each to make 135. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
5 + 10 + 9 = 135
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.501:

```text
5 + 10 - 9
```

#### countdown-test-023 / 24

Countdown puzzle: use the numbers [4, 2, 10] exactly once each to make 28. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
4 + 10 + 2 = 16  
4 + 10 + 2 = 16  
4 + 10 + 2 = 16  

(4 + 10) + 
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.505:

```text
4 + 2 - 10
```

#### countdown-test-024 / 25

Countdown puzzle: use the numbers [5, 9, 8] exactly once each to make 6. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
5 + 9 - 8 = 6
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=True; reward=1.000:

```text
5 + 9 - 8
```

#### countdown-test-025 / 26

Countdown puzzle: use the numbers [7, 13, 9] exactly once each to make 15. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
7 + 9 = 16  
13 - 16 = 15
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.530:

```text
7 + 13 - 9
```

#### countdown-test-026 / 27

Countdown puzzle: use the numbers [8, 9, 11] exactly once each to make 10. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 9 = 17  
17 - 11 = 6  
6 + 11 = 17  
17 - 8 = 9  

But the correct expression is:  
**8 +
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.530:

```text
8 + 9 - 11
```

#### countdown-test-027 / 28

Countdown puzzle: use the numbers [6, 3, 13] exactly once each to make 117. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
6 * 13 + 3 = 117
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.501:

```text
6 + 3 - 13
```

#### countdown-test-028 / 29

Countdown puzzle: use the numbers [9, 7, 8] exactly once each to make 71. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
9 + 8 + 7 = 24  
But that's not 71. Let's try again.

9 * 8 + 7 = 72  
Close, but not quite.  
9 * 8
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.502:

```text
9 + 7 - 8
```

#### countdown-test-029 / 30

Countdown puzzle: use the numbers [3, 8, 5] exactly once each to make 29. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
3 + 8 + 5 = 16  
But that's not 29. Let's try again.  

3 * 8 + 5 = 29  

**Answer:** 3 * 8 + 
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.506:

```text
3 + 8 - 5
```

#### countdown-test-030 / 31

Countdown puzzle: use the numbers [13, 12, 8] exactly once each to make 17. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
13 + 12 - 8 = 17
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=True; reward=1.000:

```text
13 + 12 - 8
```

#### countdown-test-031 / 32

Countdown puzzle: use the numbers [15, 13, 2] exactly once each to make 56. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
15 + 13 + 2 = 56
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.505:

```text
15 + 13 - 2
```

### sampled_dev

#### countdown-dev-000 / 1

Countdown puzzle: use the numbers [2, 11, 2] exactly once each to make 24. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
2 + 11 * 2 = 24
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.511:

```text
2 + 11 - 2
```

#### countdown-dev-000 / 2

Countdown puzzle: use the numbers [2, 11, 2] exactly once each to make 24. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
2 * 11 - 2 = 24
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.511:

```text
2 + 11 - 2
```

#### countdown-dev-001 / 3

Countdown puzzle: use the numbers [13, 2, 2] exactly once each to make 13. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
13 = 2 + 2 + 9
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=True; reward=1.000:

```text
13 + 2 - 2
```

#### countdown-dev-001 / 4

Countdown puzzle: use the numbers [13, 2, 2] exactly once each to make 13. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
2 + 13 = 15  
(13 - 2) = 11  
11 + 2 = 13
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=True; reward=1.000:

```text
13 + 2 - 2
```

#### countdown-dev-002 / 5

Countdown puzzle: use the numbers [10, 4, 12] exactly once each to make 18. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
12 + 6 = 18  
* – (expression format only)
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.509:

```text
10 + 4 - 12
```

#### countdown-dev-002 / 6

Countdown puzzle: use the numbers [10, 4, 12] exactly once each to make 18. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
12 + 4 = 16  
16 + 10 = 18
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.509:

```text
10 + 4 - 12
```

#### countdown-dev-003 / 7

Countdown puzzle: use the numbers [9, 9, 12] exactly once each to make 117. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
9 + 9 + 12 = 117
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.501:

```text
9 + 9 - 12
```

#### countdown-dev-003 / 8

Countdown puzzle: use the numbers [9, 9, 12] exactly once each to make 117. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
9 + 9 + 12 = 117
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.501:

```text
9 + 9 - 12
```

#### countdown-dev-004 / 9

Countdown puzzle: use the numbers [11, 7, 15] exactly once each to make 19. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
15 + 7 = 22, then subtract 3 to reach 19. (Invalid, since 3 is not used)  

Let's try again:

11 + 7 + 1 = 19
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.509:

```text
11 + 7 - 15
```

#### countdown-dev-004 / 10

Countdown puzzle: use the numbers [11, 7, 15] exactly once each to make 19. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
11 + 7 = 18  
18 + 1 = 19
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.509:

```text
11 + 7 - 15
```

#### countdown-dev-005 / 11

Countdown puzzle: use the numbers [5, 4, 10] exactly once each to make 54. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
5 + 4 + 10 = 54
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
5 + 4 - 10
```

#### countdown-dev-005 / 12

Countdown puzzle: use the numbers [5, 4, 10] exactly once each to make 54. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
5 + 4 * 10 = 54
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
5 + 4 - 10
```

#### countdown-dev-006 / 13

Countdown puzzle: use the numbers [11, 10, 12] exactly once each to make 11. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.550:

```text
11  +  12 - 10
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.550:

```text
11 + 10 - 12
```

#### countdown-dev-006 / 14

Countdown puzzle: use the numbers [11, 10, 12] exactly once each to make 11. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
11  
(12 - 10) + 1 = 11
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.550:

```text
11 + 10 - 12
```

#### countdown-dev-007 / 15

Countdown puzzle: use the numbers [4, 12, 5] exactly once each to make 68. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
4 * 12 + 5 = 68
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
4 + 12 - 5
```

#### countdown-dev-007 / 16

Countdown puzzle: use the numbers [4, 12, 5] exactly once each to make 68. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
4 + 12 + 5 = 21  
But that's only 21, not 68. Let me check again. 

Wait, maybe the puzzle is asking for the expression that evaluates to 68
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
4 + 12 - 5
```

#### countdown-dev-008 / 17

Countdown puzzle: use the numbers [8, 2, 4] exactly once each to make 16. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 2 + 4 = 14  
8 + 2 * 4 = 14  
8 * (2 + 4) = 16
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.514:

```text
8 + 2 - 4
```

#### countdown-dev-008 / 18

Countdown puzzle: use the numbers [8, 2, 4] exactly once each to make 16. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 2 + 4 = 14  
Maybe adjust: 8 + 4 + 2 = 14  
Correct: 8 + 4 + 2 = 14

Wait, but the correct
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.514:

```text
8 + 2 - 4
```

#### countdown-dev-009 / 19

Countdown puzzle: use the numbers [6, 7, 12] exactly once each to make 54. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
6 * 7 + 12 = 54
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
6 + 7 - 12
```

#### countdown-dev-009 / 20

Countdown puzzle: use the numbers [6, 7, 12] exactly once each to make 54. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
6 * 7 + 12 = 54
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
6 + 7 - 12
```

#### countdown-dev-010 / 21

Countdown puzzle: use the numbers [6, 2, 15] exactly once each to make 36. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
6 * 2 + 15 = 36
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
6 + 2 - 15
```

#### countdown-dev-010 / 22

Countdown puzzle: use the numbers [6, 2, 15] exactly once each to make 36. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
6 + 15 + 2 = 23
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.503:

```text
6 + 2 - 15
```

#### countdown-dev-011 / 23

Countdown puzzle: use the numbers [8, 14, 5] exactly once each to make 117. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
14 + 8 * 5 = 117
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.501:

```text
8 + 14 - 5
```

#### countdown-dev-011 / 24

Countdown puzzle: use the numbers [8, 14, 5] exactly once each to make 117. Allowed operations: + - * / and parentheses. Return ONLY the arithmetic expression. No equals sign, answer, code fence, or explanation.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
8 + 14 + 5 = 27  
(8 * 14) + 5 = 117
```

After — Qwen/Qwen3-0.6B + countdown RLVR; success=False; reward=0.501:

```text
8 + 14 - 5
```

## maze: rlvr-train-maze-1788799930241701161

Model: **Qwen/Qwen3-0.6B**, revision `c1899de289a04d12100db370d81485cdf75e47ca`. After: RLVR on this task only, 160 batches / 4 updates, rank-16 LoRA, LR 0.0002, beta 0. Selected batch 160; checkpoint selection disabled (final batch). Data SHA-256 `056e75da0338d4d6bebdf6071558593d4a192737897ed98522d298446106cf1b`. Fresh-base adapter reload matches: True.

Sampling uses temperature 1, top-k 0, top-p 1; evaluation seed 2026. Greedy evaluation uses batches of eight. No decoding repair or retry.

### dev

#### maze-dev-000 / 1

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..S.
..#.
.#..
..G.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-001 / 2

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
G..S
.#..
#...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G..S

(Explanation: The robot starts at G, moves to S, and the path is clear. The final move is "G..S".
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-002 / 3

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
...S
#...
...#
..G.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-003 / 4

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
...S
#...
.G..
..#.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-004 / 5

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..S.
....
G.#.
...#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-005 / 6

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
G..#
....
....
..S#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G..#  
....  
....  
....  
S#  
....  
....  
....  
....  
....  
....  
....  
....  
....  
....
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-006 / 7

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..##
..S.
G...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-007 / 8

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
#..G
S...
#...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D R L
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-008 / 9

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
.G.#
...#
..S.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#L.
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-009 / 10

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
G.#.
..#.
....
..S.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#.#  
..#  
....  
..S.
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-010 / 11

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.S.#
...G
#...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#L.
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-011 / 12

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
##.G
....
.S..

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
**Move:** U D L R

Explanation:
- Start at S.
- Move up to .G (position (1,1)).
- Move down to
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-012 / 13

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..S#
....
G#..
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-013 / 14

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
#S..
#...
....
.G..

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-014 / 15

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
S..#
..G.
....
#...

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
Move the robot from S to G on the 4x4 map:

**U**  
**U**  
**U**  
**U**  

This
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-015 / 16

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
..S.
G##.
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
The robot starts at position **S** and needs to reach position **G** on the 4x4 map. Here's the path:

- Start at
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-016 / 17

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
G#..
....
..S.
.#..

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#..  
....  
..S.  
.#..
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-017 / 18

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.S..
#...
.#.G
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-018 / 19

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
#.G.
S...
.#..
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G S . .
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-019 / 20

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
#..S
....
G...
#...

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-020 / 21

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.S.#
...G
.#..
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-021 / 22

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
.#..
.S..
..#G

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
`U D L R`
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-022 / 23

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
S.#.
....
.G#.
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-023 / 24

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
#..G
.#..
S...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

### test

#### maze-test-000 / 1

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
S...
....
....
G.##

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
Move a robot from S to G on the 4x4 map:

**U**  
**U**  
**U**  
**U**  

**
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-001 / 2

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
#.S.
....
...G
...#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D R L
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-002 / 3

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..G.
....
.S..
#.#.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G S . .  
. . . .  
.S..  
# . # .  

Move sequence: **U D L R**
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-003 / 4

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.S..
#...
G...
.#..

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#L.
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-004 / 5

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.S..
..#.
G...
..#.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#L.
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-005 / 6

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
S...
....
.#G#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#.#
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-006 / 7

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.G.#
#...
..S.
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#...  
#...  
..S.  
....
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-007 / 8

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.G..
....
..#.
.S.#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G S . .
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-008 / 9

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.G.#
....
....
.#.S

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#.#  
....  
....  
.#.S

Move: G#.#  
....  
....  
.#.S
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-009 / 10

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.S#.
....
....
.G#.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#G#  
....  
....  
....
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-010 / 11

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..G.
...#
....
.S#.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G

Explanation: The robot starts at position S and moves to G. The path is clear, and the robot does not enter any walls. The final move
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-011 / 12

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
G...
.#S.
...#
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G...  
.#S.  
...#  
....
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-012 / 13

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..S.
G...
....
#..#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-013 / 14

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
S##.
...G
....
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-014 / 15

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
.S..
..##
..G.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
**Move:** U D L R

Explanation:
- Start at S (position (0,0))
- Move up to U (position (0,1
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-015 / 16

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.#..
S#..
....
..G.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#L

Explanation:  
- Start at S (row 0, column 1).  
- Move down to G (row 3, column
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-016 / 17

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
...G
...#
.S..
...#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G S . .
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-017 / 18

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
S.#G
....
.#..

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
**Move:** U D L R

Explanation:
- Start at S (row 0, column 0)
- Move U to row 0, column
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-018 / 19

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..#.
G...
....
..#S

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-019 / 20

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..S.
....
.#..
..#G

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-020 / 21

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
#...
#..S
G...

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
The robot starts at position **S** and needs to reach position **G** on the 4x4 map. Here's the path:

- Start at
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-021 / 22

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..S.
#...
....
G..#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G R U D
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-022 / 23

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
...#
...#
G...
...S

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-023 / 24

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..#.
..S.
...#
...G

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-024 / 25

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
S..#
..#G
....
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D R L
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-025 / 26

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
S#.G
...#
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#S

Explanation:  
- Start at position S (row 0, column 0).  
- Move to G (row 1, column
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-026 / 27

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
S...
..#.
#...
.G..

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-test-027 / 28

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
...G
.#..
S..#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#S..
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-028 / 29

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
#...
..S.
G..#
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
The robot moves from S to G on the 4x4 map:

# . . S .  
G . . #  
. . . .  
.
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-029 / 30

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
...#
S...
..G#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-030 / 31

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..#.
.G#.
....
..S.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-test-031 / 32

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.#.#
..G.
....
...S

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

### sampled_dev

#### maze-dev-000 / 1

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..S.
..#.
.#..
..G.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U L R D
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-000 / 2

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..S.
..#.
.#..
..G.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
L R U D
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-001 / 3

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
G..S
.#..
#...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G...S

(Answer: G...S)
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-001 / 4

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
G..S
.#..
#...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D R U D L
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-002 / 5

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
...S
#...
...#
..G.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G D U L
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-002 / 6

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
...S
#...
...#
..G.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D R Ł
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-003 / 7

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
...S
#...
.G..
..#.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G D U L
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-003 / 8

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
...S
#...
.G..
..#.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
"U"  U
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-004 / 9

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..S.
....
G.#.
...#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
Move: U D R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-004 / 10

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..S.
....
G.#.
...#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-005 / 11

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
G..#
....
....
..S#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G R U L
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-005 / 12

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
G..#
....
....
..S#

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G L R U
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-006 / 13

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..##
..S.
G...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
Move the robot from S to G on this 4x4 map:

U

The robot moves up, then:

U

Then:

U

Then:


```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-006 / 14

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
..##
..S.
G...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
"U D L R U R L"
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-007 / 15

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
#..G
S...
#...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D L R
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-007 / 16

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
#..G
S...
#...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
GSD...
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-008 / 17

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
.G.#
...#
..S.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
G#..#

G. . . 

G. . . 

. . S.
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-008 / 18

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
.G.#
...#
..S.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
`.G.#`  
`...#`  
`...#`  
`..S.`  

**Robot moves from S to G.**  
Moves:
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-009 / 19

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
G.#.
..#.
....
..S.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U D R L
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-009 / 20

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
G.#.
..#.
....
..S.

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
U R D R U
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-010 / 21

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.S.#
...G
#...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
`.SGW`
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-010 / 22

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
.S.#
...G
#...
....

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
R L U D
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.100:

```text
UD
```

#### maze-dev-011 / 23

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
##.G
....
.S..

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
**Answer:** U R D L

This path moves the robot from S to G without crossing walls or leaving the map.
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```

#### maze-dev-011 / 24

Move a robot from S to G on this 4x4 map. # is a wall; . is free. U=up, D=down, L=left, R=right. Never enter walls or leave the map. Return ONLY a string of at most 12 moves using U, D, L, R. No spaces or explanation.
....
##.G
....
.S..

Before — original Qwen/Qwen3-0.6B; success=False; reward=0.000:

```text
The robot starts at **S** and must reach **G** on the 4x4 grid:

```
. 
. 
.S.
. 
``
```

After — Qwen/Qwen3-0.6B + maze RLVR; success=False; reward=0.300:

```text
UD
```
