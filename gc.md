The `mung-gc [tree]` command runs a garbage collector over the master history directory `$MUNG_ALL_histories` and makes the files in the tree agree with the histories.  This happens when the file being munged is deleted but the history is not removed.

Here's what is done.  Read through the directory of all histories, which is $MUNG_ALL_HISTORIES (or by default $HOME/.mung)   The file whose pathname appears in "filename" in each history directory is checked to determine its device and inode numbers, which are an absolute identification of the file (they do not change if the file is renamed or rewritten).  If the file exists and its device and inode numbers match the name of the history directory, all is well, and we move on to the next history.

Then, if the file exists, ask about moving it somewhere else (prompt for the new name).  If it does not exist, ask about restoring it from the current state. In either case, ask about destroying the history.

