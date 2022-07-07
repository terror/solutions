class Solution
  def solve(s)
    i = 0
    ans = ''
    while i < s.length()
      curr = ''

      while s[i].match(/[0-9]/)
        curr += s[i]
        i += 1
      end

      for _ in 0..curr.to_i - 1
        ans += s[i]
      end

      i += 1
    end

    return ans
  end
end
