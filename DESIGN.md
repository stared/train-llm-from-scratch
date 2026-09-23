---
version: alpha
colors:
  background: "#ffffff"
  text: "#242a2d"
  muted: "#697477"
  line: "#e1e5e5"
  primary: "#236c70"
typography:
  sans:
    fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "15px"
    lineHeight: "1.55"
  mono:
    fontFamily: 'ui-monospace, SFMono-Regular, Consolas, monospace'
rounded:
  control: "4px"
spacing:
  page-max: "1180px"
  page-padding: "36px"
  mobile-padding: "18px"
---

# Workshop viewer

## Overview

A quiet teaching tool for first-time model trainers. English controls surround Polish training examples. The main task is comparing recorded outputs and metrics across checkpoints. The chapter guides define the workflows; this document records existing UI conventions, not a redesign.

## Colors

Runtime styling is owned by `visualization/style.css`; the values above document its current baseline. The teal accent highlights training progress. Text labels distinguish Running, Completed and Example run; color alone must not carry status.

## Typography

Use the existing system font stack for controls and headings. Use monospace for prompts and generated text. Preserve Polish characters and wrapping.

## Layout

Keep the document scrollable and the existing mobile breakpoint at 700px. The numbered navigation follows the workshop chapters. Charts and before/after examples are the visual focus.

## Elevation & Depth

Use flat sections and divider lines. Recovery messages do not need overlays or modal dialogs.

## Shapes

Keep the existing four-pixel control corners and native select menus.

## Components

- `visualization/app.js` owns shared run selection and status across pretraining, SFT and RLVR. `server.catalog()` preserves a live run's public ID when its saved result appears.
- `visualization/index.html` owns the startup message and Reload page button, independently of application-module loading. Use a status region and an actionable failure message; never leave a blank shell on module failure.
- Existing native buttons/selects retain keyboard behavior and the focus indicator from `style.css`.
- `Handler.reply()` serves fresh HTML, JavaScript and API responses with `Cache-Control: no-store`.

## Do's and Don'ts

Use short instructions, preserve the selected run through completion, and keep recovery under the user's control. Do not automatically reload a working page or discard an entered prompt on server restart. Test with local fixtures; viewing results must not launch training.
