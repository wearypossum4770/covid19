import { useState } from "react";
const useStateOnlyExample = () => {
  const [first, setFirst] = useState("alpha");
  const [second, setSecond] = useState("beta");
  const [third, setThird] = useState(() => "charlie"); // Notice the delayed execution
  const update = () => {
    setFirst(first + "a");
    setSecond(second + "b");
    setThird(third + "c");
  };
  return { first, second, third, update };
};
