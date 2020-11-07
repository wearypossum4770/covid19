import { useState, useReducer, useCallback, useEffect } from "react";
export const useFetch = (url, initialValue) => {
  const init = {
    ...initialValue,
    isLoading: true,
    data: null,
    errors: null,
  };
  function reducer(state, action) {
    switch (action.type) {
      case "SET_LOADING":
        return { ...state, isLoading: true };
      case "SET_ERROR":
        return { ...state, errors: action.payload };
      case "SET_LOADED":
        return { ...state, isLoading: false };
      case "SET_DATA":
        return { ...state, data: action.payload };
      default:
        return { ...state };
    }
  }
  const [state, dispatch] = useReducer(reducer, init);
  const fetchData = useCallback(async () => {
    try {
      dispatch({ type: "SET_LOADING" });
      const response = await (await fetch(url)).json();
      if (response.status === 200) {
        dispatch({ type: "SET_DATA", payload: response.data });
      }
    } catch (error) {
      dispatch({ type: "SET_ERROR", payload: error });
      throw error
    } finally {
      dispatch({ type: "SET_LOADED" });
    }
  },[url]);
useEffect(()=>{
  fetchData()
}, [fetchData])
return state
};
