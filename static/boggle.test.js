boggle5 = new GameOBoggle('boggle', 60, 5)
boggle6 = new GameOBoggle('boggle', 60, 6)

describe('assign points', () => {
    it('should assign points correctly in a 5x5 board', () => {
        expect(boggle5.scoreWord('fish')).toEqual(2);
        expect(boggle5.scoreWord('horses')).toEqual(5);
        expect(boggle5.scoreWord('jacuzzis')).toEqual(10);
        expect(boggle5.scoreWord('abandoned')).toEqual(12);
    });
    it('should assign points correctly in a 6x6 board', () => {
        expect(boggle6.scoreWord('fish')).toEqual(1);
        expect(boggle6.scoreWord('horses')).toEqual(3);
        expect(boggle6.scoreWord('jacuzzis')).toEqual(5);
        expect(boggle6.scoreWord('abandoned')).toEqual(10);
        expect(boggle6.scoreWord('abbreviate')).toEqual(12);
        expect(boggle6.scoreWord('abbreviated')).toEqual(14);
    });
});

