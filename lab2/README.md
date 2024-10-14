# FIA Laboratory Work No. 2
## Topic: (Intelligent) Searching Algorithms

### Tasks:
1. [x] Implement the MiniMax Algorithm with the following scoring function
    `Score = Pallet_Score - Ghost_Danger`
    where:
    - `Pallet_Score` - the distance to the closest pallet (food);
    - `Ghost_Danger` - the distance to the nearest ghost.
2. [x] Implement Alpha-Beta Pruning.
3. [x] Implement an improved scoring (evaluation) method for MiniMax. For example, you could add values like MazeComplexity, PalletNumber per region or GhostVulnerability. Be creative!
`Note: you can get bonuses implementing adding more characteristics to the evaluation. For the second scoring improvement you get 0.5p, for 3rd you get 0.25p, for 4th- 0.125p and so on...`
4. [ ] Add at least one improvement to the MiniMax algorithm from the following list: Progressive Deepening, Transposition Tables, Opening Books, Move Ordering, Aspiration Window, etc.
`Note: you can get bonuses for implementing more improvements. For the second improvement you get 0.5p, for 3rd you get 0.25p, for 4th- 0.125p and so on...`
5. [ ] Improve the Path Finding algorithm for the Agent using the A-Star algorithm. Combine it with the implemented MiniMax algorithm.
6. [ ] Combine it with the implemented Alpha-Beta Pruning algorithm.
