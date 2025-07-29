#!/bin/bash

# Script to sync fyoutube repository from upstream mbeware/fyoutube
# This script should be run at session startup to keep the repo up to date

set -e  # Exit on any error

REPO_DIR="/home/ubuntu/repos/fyoutube"
UPSTREAM_REMOTE="upstream"
UPSTREAM_URL="https://github.com/mbeware/fyoutube.git"

echo "🔄 Syncing fyoutube repository from upstream..."

# Change to repository directory
cd "$REPO_DIR"

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

# Add upstream remote if it doesn't exist
if ! git remote get-url "$UPSTREAM_REMOTE" >/dev/null 2>&1; then
    echo "➕ Adding upstream remote: $UPSTREAM_URL"
    git remote add "$UPSTREAM_REMOTE" "$UPSTREAM_URL"
else
    echo "✅ Upstream remote already exists"
fi

# Fetch latest changes from upstream
echo "📥 Fetching latest changes from upstream..."
git fetch "$UPSTREAM_REMOTE"

# Get current branch name
CURRENT_BRANCH=$(git branch --show-current)
echo "📍 Current branch: $CURRENT_BRANCH"

# Check if there are any uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "⚠️  Warning: You have uncommitted changes. Stashing them..."
    git stash push -m "Auto-stash before upstream sync $(date)"
    STASHED=true
else
    STASHED=false
fi

# Merge or rebase upstream changes
echo "🔀 Merging upstream changes..."
if git merge "$UPSTREAM_REMOTE/$CURRENT_BRANCH" --no-edit; then
    echo "✅ Successfully merged upstream changes"
else
    echo "⚠️  Merge conflicts detected. Please resolve manually."
    echo "   Run 'git status' to see conflicted files"
    echo "   After resolving conflicts, run 'git commit' to complete the merge"
    exit 1
fi

# Restore stashed changes if any
if [ "$STASHED" = true ]; then
    echo "📤 Restoring your stashed changes..."
    if git stash pop; then
        echo "✅ Stashed changes restored successfully"
    else
        echo "⚠️  Conflicts while restoring stashed changes. Please resolve manually."
        echo "   Your changes are still in the stash. Run 'git stash list' to see them."
    fi
fi

echo "🎉 Repository sync completed successfully!"
echo "📊 Latest commits:"
git log --oneline -5