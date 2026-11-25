---
description: Prepare a new AppFootings release (version bump, changelog, package, tag)
argument-hint: "[major|minor|patch]"
---

Prepare a release of type $ARGUMENTS (if empty, propose one based on the changes since the last tag, using the semver rules in CHANGELOG.md).

1. Run `/consistency-check` and stop if anything is not aligned.
2. Summarise the changes since the last tag (`git log`), and draft the CHANGELOG entry (Added / Changed / Fixed).
3. Bump `VERSION`.
4. If anything in the screens, the example or the images changed, regenerate images, GIF and prototype with `python3 scripts/make_images.py`.
5. Run `scripts/package.sh` and `scripts/install-local.sh`.
6. Show me the CHANGELOG entry and the list of changed files, and wait for my OK.
7. After my OK: commit "Release vX.Y.Z", create the tag `vX.Y.Z`, push the branch and the tag. The GitHub workflow publishes the zip.
